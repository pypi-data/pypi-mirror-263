import logging
import os
import pathlib
import sys

import pyarrow.flight
import yaml

from kywy.server.kawa_flight_server import KawaFlightServer

from kywy.server.kawa_log_manager import default_dict_logging_config, default_job_logging_level, \
    default_job_logging_formatter


def start_server():
    if len(sys.argv) < 2:
        aes_key = None
        if os.getenv('KAWA_AUTOMATION_SERVER_AES_KEY'):
            aes_key = os.getenv('KAWA_AUTOMATION_SERVER_AES_KEY')
        elif os.getenv('KAWA_AUTOMATION_SERVER_AES_KEY_FILE'):
            with open(os.getenv('KAWA_AUTOMATION_SERVER_AES_KEY_FILE'), 'r') as f:
                aes_key = f.read().strip()
        if not aes_key:
            raise Exception('Specify either KAWA_AUTOMATION_SERVER_AES_KEY or KAWA_AUTOMATION_SERVER_AES_KEY_FILE')

    else:
        aes_key = sys.argv[1]

    # Logging configuration

    dict_logging_config = default_dict_logging_config()
    if os.getenv('KAWA_AUTOMATION_SERVER_LOGGING_CONFIG'):
        with open(os.getenv('KAWA_AUTOMATION_SERVER_LOGGING_CONFIG'), 'r') as yaml_logging_config_file:
            dict_logging_config = yaml.safe_load(yaml_logging_config_file)
    job_logging_level = default_job_logging_level()
    if os.getenv('KAWA_AUTOMATION_SERVER_JOB_LOGGING_LEVEL'):
        job_logging_level = os.getenv('KAWA_AUTOMATION_SERVER_JOB_LOGGING_LEVEL')
    job_logging_formatter = default_job_logging_formatter()
    if os.getenv('KAWA_AUTOMATION_SERVER_JOB_LOGGING_FORMATTER'):
        job_logging_formatter = os.getenv('KAWA_AUTOMATION_SERVER_JOB_LOGGING_FORMATTER')
    logging.config.dictConfig(dict_logging_config)

    # Flight server
    host = os.getenv('KAWA_AUTOMATION_SERVER_HOST') or '0.0.0.0'
    port = int(os.getenv('KAWA_AUTOMATION_SERVER_PORT') or 8815)

    # KAWA server

    kawa_url = os.getenv('KAWA_URL')
    if not kawa_url:
        raise Exception('Specify KAWA_URL: this is the URL to reach KAWA server (from this server)')

    if os.getenv('KAWA_AUTOMATION_SERVER_USER_TLS'):
        location = pyarrow.flight.Location.for_grpc_tls(host=host, port=port)
        tls_cert_path = os.getenv('KAWA_AUTOMATION_SERVER_TLS_CERT_PATH')
        tls_key_path = os.getenv('KAWA_AUTOMATION_SERVER_TLS_KEY_PATH')
        if tls_cert_path and tls_key_path:
            with pathlib.Path(tls_cert_path).open("rb") as tls_cert_file:
                tls_cert = tls_cert_file.read()
            with pathlib.Path(tls_key_path).open("rb") as tls_key_file:
                tls_key = tls_key_file.read()
            tls_certificates = [
                pyarrow.flight.CertKeyPair(cert=tls_cert, key=tls_key)
            ]
        else:
            tls_certificates = []
    else:
        # Not TLS
        location = pyarrow.flight.Location.for_grpc_tcp(host=host, port=port)
        tls_certificates = []

    working_directory_path = os.getenv('KAWA_AUTOMATION_SERVER_WORKING_DIRECTORY') or '/tmp'
    working_directory = pathlib.Path(working_directory_path)

    server = KawaFlightServer(
        dict_logging_config=dict_logging_config,
        job_logging_level=job_logging_level,
        job_logging_formatter=job_logging_formatter,
        location=location,
        working_directory=working_directory,
        tls_certificates=tls_certificates,
        aes_key=aes_key,
        kawa_url=kawa_url
    )
    server.serve()


if __name__ == '__main__':
    start_server()
