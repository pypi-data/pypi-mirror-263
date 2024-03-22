import concurrent.futures
import logging

import pandas as pd
import pyarrow as pa
import json

from kywy.client.kawa_client import KawaClient
from kywy.scripts.kawa_loader_callback import LoaderCallback
from kywy.server.clear_script_with_secrets import ClearScriptWithSecrets
from kywy.server.interpreter_error import InterpreterError
from kywy.server.kawa_directory_manager import KawaDirectoryManager
from kywy.server.kawa_error_manager import KawaErrorManager
from kywy.server.kawa_log_manager import KawaLogManager, get_kawa_logger


def _get_executable(clear_script_with_secrets: ClearScriptWithSecrets):
    scope = {}
    exec(clear_script_with_secrets.clear_script, scope, scope)
    functions_in_scope_with_inputs = [v for v in scope.values() if hasattr(v, 'inputs')]
    if len(functions_in_scope_with_inputs) == 0:
        raise InterpreterError('The python script provided does not contain any function with inputs defined with '
                               'the @inputs decorator')
    if len(functions_in_scope_with_inputs) > 1:
        raise InterpreterError('The python script provided contain more than one function with defined inputs')
    final_function = functions_in_scope_with_inputs[0]
    inputs_provided_by_kawa = ['df', 'kawa']
    if hasattr(final_function, 'secrets'):
        secret_mapping = dict(final_function.secrets)
        inputs_provided_by_kawa.extend(secret_mapping.keys())
        if 'kawa' in secret_mapping:
            raise InterpreterError('kawa is a reserved name for the KawaClient and cannot be used in secrets')
        if 'df' in secret_mapping:
            raise InterpreterError('df is a reserved name for the DataFrame input and cannot be used in secrets')
    necessaries_inputs = final_function.__code__.co_varnames[:final_function.__code__.co_argcount]
    missing_arguments = set(necessaries_inputs).difference(inputs_provided_by_kawa)
    if len(missing_arguments) != 0:
        raise InterpreterError('Some arguments defined in the main function: {} are not defined. The list : {}'
                               .format(final_function.__name__, missing_arguments))
    return final_function


def _execute_script(job_id: str,
                    job_log_file: str,
                    kawa_log_manager: KawaLogManager,
                    clear_script_with_secrets: ClearScriptWithSecrets,
                    arrow_table: pa.Table,
                    callback: LoaderCallback,
                    kawa_client: KawaClient):
    # This function is executed as a separated process.
    # It must be an independent function (not an object method), and its parameters must be serializable.
    # The instantiated script can't be serialized, hence the function is called with the script source code (str).

    kawa_log_manager.configure_root_logger_of_job_process(job_log_file)
    kawa_logger = get_kawa_logger()
    if callback:
        kawa_logger.info('Job: %s, execute script with callback', job_id)
    else:
        kawa_logger.info('Job: %s, execute script without callback', job_id)
    current_step = ''
    try:
        current_step = 'extracting executable'
        # the function that will be executed
        function = _get_executable(clear_script_with_secrets)
        # the available parameters (df, kawa and the secrets)
        available_parameters = {'df': arrow_table.to_pandas(), 'kawa': kawa_client}
        if hasattr(function, 'secrets'):
            available_parameters.update({param: clear_script_with_secrets.kawa_secrets.get(key_secret)
                                         for param, key_secret in function.secrets.items()})
        # get the function parameters
        necessary_parameters = function.__code__.co_varnames
        # now keep only the necessaries parameters
        final_parameters = {k: v for k, v in available_parameters.items() if k in necessary_parameters}
        current_step = 'executing the script'
        # now apply the parameters to the function
        output_df = function(**final_parameters)
        kawa_logger.info('Script execution finished')

        if callback:
            current_step = 'loading the resulting dataframe into Kawa'
            if isinstance(output_df, pd.DataFrame):
                callback.load(output_df)
            else:
                raise InterpreterError('Script must return a pandas.DataFrame')
        return True

    except Exception as e:
        kawa_logger.error('Error while {}: '.format(current_step), exc_info=1)
        raise e

    finally:
        root_logger = logging.getLogger()
        kawa_log_manager.remove_all_handlers(root_logger)


class KawaScriptManager:

    def __init__(self,
                 kawa_url,
                 kawa_directory_manager: KawaDirectoryManager,
                 kawa_log_manager: KawaLogManager,
                 kawa_error_manager: KawaErrorManager):
        self.kawa_url = kawa_url
        self.executor = concurrent.futures.ProcessPoolExecutor()
        self.directory_manager = kawa_directory_manager
        self.kawa_log_manager = kawa_log_manager
        self.error_manager = kawa_error_manager

    def get_script_metadata(self, clear_script_with_secrets: ClearScriptWithSecrets):
        try:
            script_meta = self._get_function_metadata(clear_script_with_secrets)
            json_meta = json.dumps(script_meta)
            get_kawa_logger().debug('Script metadata: %s', json_meta)
            return json_meta
        except Exception as err:
            self.error_manager.rethrow(err)

    def submit_script_for_execution(self,
                                    job_id: str,
                                    principal: str,
                                    clear_script_with_secrets: ClearScriptWithSecrets,
                                    action_payload,
                                    arrow_table: pa.Table) -> concurrent.futures.Future:
        kawa_client = self._create_kawa_client(action_payload)
        callback = self._create_callback(action_payload, kawa_client)
        job_log_file = self.directory_manager.log_path(job_id, principal)
        return self.executor.submit(
            _execute_script,
            job_id,
            job_log_file,
            self.kawa_log_manager,
            clear_script_with_secrets,
            arrow_table,
            callback,
            kawa_client
        )

    def _get_function_metadata(self, clear_script_with_secrets: ClearScriptWithSecrets):
        func = _get_executable(clear_script_with_secrets)
        return {
            'parameters': func.inputs,
            'outputs': func.outputs if hasattr(func, 'outputs') else []
        }

    def _create_callback(self, action_payload, kawa_client: KawaClient):
        if action_payload.get('pythonPrivateJoinId'):
            python_private_join_id = action_payload.get('pythonPrivateJoinId')
            pk_params = action_payload.get('pkParams')
            pk_mapping_indicator_ids = action_payload.get('pkMappingIndicatorIds')
            job_id = str(action_payload['job']).split('|')[1]
            return LoaderCallback(python_private_join_id,
                                  pk_params,
                                  pk_mapping_indicator_ids,
                                  job_id,
                                  kawa_client)
        else:
            return None

    def _create_kawa_client(self, action_payload) -> KawaClient:
        workspace_id = action_payload.get('workspaceId')
        api_key = action_payload.get('apiKey')
        kawa_client = KawaClient(kawa_api_url=self.kawa_url)
        kawa_client.set_api_key(api_key=api_key)
        kawa_client.set_active_workspace_id(workspace_id=workspace_id)
        return kawa_client
