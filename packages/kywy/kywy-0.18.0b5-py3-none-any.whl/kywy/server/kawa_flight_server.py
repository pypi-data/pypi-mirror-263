import concurrent.futures
import json
import logging
import traceback

import pyarrow as pa
import pyarrow.flight
import pyarrow.parquet

from kywy.server.clear_script_with_secrets import ClearScriptWithSecrets
from kywy.server.interpreter_error import InterpreterError
from kywy.server.kawa_directory_manager import KawaDirectoryManager
from kywy.server.kawa_error_manager import KawaErrorManager
from kywy.server.kawa_jobs_manager import KawaJobsManager
from kywy.server.kawa_log_manager import KawaLogManager, get_kawa_logger
from kywy.server.kawa_script_manager import KawaScriptManager


class KawaFlightServer(pa.flight.FlightServerBase):

    def __init__(self,
                 dict_logging_config,
                 job_logging_level,
                 job_logging_formatter,
                 location=None,
                 working_directory=None,
                 tls_certificates=None,
                 aes_key=None,
                 kawa_url=None,
                 **kwargs):
        super(KawaFlightServer, self).__init__(location=location, tls_certificates=tls_certificates, **kwargs)
        self._location = location
        self._aes_key = aes_key
        self.kawa_url = kawa_url
        self.executor = concurrent.futures.ProcessPoolExecutor()

        self.error_manager = KawaErrorManager()
        self.directory_manager = KawaDirectoryManager(working_directory, self.error_manager)
        self.jobs_manager = KawaJobsManager(self.directory_manager, self.error_manager)
        self.log_manager = KawaLogManager(
            dict_logging_config,
            job_logging_level,
            logging.Formatter(job_logging_formatter)
        )
        self.script_manager = KawaScriptManager(kawa_url, self.directory_manager, self.log_manager, self.error_manager)

        get_kawa_logger().info('KAWA Python automation server started at location: %s', self._location)

    def _make_flight_info(self, job_id):
        schema = pa.parquet.read_schema(self.directory_manager.dataset_path(job_id))
        metadata = pa.parquet.read_metadata(self.directory_manager.dataset_path(job_id))
        descriptor = pa.flight.FlightDescriptor.for_path(
            job_id.encode('utf-8')
        )
        endpoints = [pa.flight.FlightEndpoint(job_id, [self._location])]
        return pyarrow.flight.FlightInfo(schema,
                                         descriptor,
                                         endpoints,
                                         metadata.num_rows,
                                         metadata.serialized_size)

    def list_flights(self, context, criteria):
        raise InterpreterError('Not supported')

    def get_flight_info(self, context, descriptor):
        return self._make_flight_info(descriptor.path[0].decode('utf-8'))

    def do_put(self, context, descriptor, reader, writer):
        job_id = descriptor.path[0].decode('utf-8')
        data_table = reader.read_all()
        get_kawa_logger().info('Upload dataset for job: %s', job_id)
        self.directory_manager.write_table(job_id, data_table)

    def do_get(self, context, ticket):
        job_id = ticket.ticket.decode('utf-8')
        get_kawa_logger().info('Download dataset for job: %s', job_id)
        return pa.flight.RecordBatchStream(self.directory_manager.read_table(job_id))

    def list_actions(self, context):
        return [
            ('run_script', 'Queue an automation script for execution.'),
            ('restart_script', 'Restart an already uploaded script.'),
            ('script_metadata', 'Get automation script metadata (parameters, outputs).'),
            ('poll_jobs', 'Poll status of specific queued jobs.'),
            ('health', 'Check server health.'),
        ]

    def do_action(self, context, action):
        try:
            get_kawa_logger().debug('action.type: %s', action.type)
            if action.type == 'run_script':
                self.action_run_script(action)
            elif action.type == 'script_metadata':
                json_result = self.action_script_metadata(action)
                return self.json_to_array_of_one_flight_result(json_result)
            elif action.type == 'poll_jobs':
                json_result = self.action_poll_jobs(action)
                return self.json_to_array_of_one_flight_result(json_result)
            elif action.type == 'get_job_log':
                json_result = self.action_get_job_log(action)
                return self.json_to_array_of_one_flight_result(json_result)
            elif action.type == 'delete_job':
                self.action_delete_job(action)
            elif action.type == 'health':
                # Improve it later
                return self.json_to_array_of_one_flight_result('{"status":"OK"}')
            else:
                raise NotImplementedError
        except Exception as err:
            traceback.print_exception(err)
            self.error_manager.rethrow(err)

    def action_run_script(self, action):
        try:
            json_action_payload = self.parse_action_payload(action)
            job_id = json_action_payload['job']
            principal = json_action_payload['principal']
            encrypted_script_with_secrets = json_action_payload['script']
            self.directory_manager.write_encrypted_script(job_id, encrypted_script_with_secrets)
            self.do_submit_script_for_execution(job_id, principal, encrypted_script_with_secrets, json_action_payload)
        except Exception as err:
            self.error_manager.rethrow(err)

    def action_script_metadata(self, action):
        json_action_payload = self.parse_action_payload(action)
        encrypted_script_with_secrets = json_action_payload['script']
        clear_script_with_secrets = ClearScriptWithSecrets.decrypt(encrypted_script_with_secrets, self._aes_key)
        return self.script_manager.get_script_metadata(
            clear_script_with_secrets=clear_script_with_secrets
        )

    def action_poll_jobs(self, action):
        json_action_payload = self.parse_action_payload(action)
        poll_jobs = json_action_payload['jobs']
        return json.dumps(self.jobs_manager.poll_jobs(poll_jobs))

    def action_get_job_log(self, action):
        json_action_payload = self.parse_action_payload(action)
        job_id = json_action_payload['job']
        principal = json_action_payload['principal']
        return json.dumps(self.jobs_manager.get_job_log(job_id, principal))

    def action_delete_job(self, action):
        json_action_payload = self.parse_action_payload(action)
        job_id = json_action_payload['job']
        principal = json_action_payload['principal']
        self.jobs_manager.delete_job(job_id, principal)

    def do_submit_script_for_execution(self,
                                       job_id: str,
                                       principal: str,
                                       encrypted_script_with_secrets: str,
                                       json_action_payload):
        clear_script_with_secrets = ClearScriptWithSecrets.decrypt(encrypted_script_with_secrets, self._aes_key)
        future = self.script_manager.submit_script_for_execution(
            job_id=job_id,
            principal=principal,
            clear_script_with_secrets=clear_script_with_secrets,
            action_payload=json_action_payload,
            arrow_table=self.directory_manager.read_table(job_id)
        )
        future.add_done_callback(lambda f: self.on_run_script_complete(f, job_id))
        self.jobs_manager.add_job(job_id, future)

    def on_run_script_complete(self, future, job_id):
        get_kawa_logger().debug('Script execution complete, for job: %s', job_id)
        self.directory_manager.remove_job_working_files(job_id)

    @staticmethod
    def json_to_array_of_one_flight_result(json_result: str):
        flight_result = pyarrow.flight.Result(pyarrow.py_buffer(json_result.encode('utf-8')))
        return [flight_result]

    @staticmethod
    def parse_action_payload(action: pyarrow.flight.Action):
        return json.loads(action.body.to_pybytes().decode('utf-8'))
