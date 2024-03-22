import logging
import logging.config
import logging.handlers
import multiprocessing
import threading


def get_kawa_logger():
    return logging.getLogger('kawa')


def logger_thread_function(q: multiprocessing.Queue):
    while True:
        record = q.get()
        if record is None:
            break
        logger = logging.getLogger(record.name)
        logger.handle(record)


def default_job_logging_level():
    return logging.DEBUG


def default_job_logging_formatter():
    return '%(asctime)s - %(name)s - %(levelname)s - %(message)s'


def default_dict_logging_config():
    return {
            'version': 1,
            'formatters': {
                'simple': {
                    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
                }
            },
            'handlers': {
                'console': {
                    'class': 'logging.StreamHandler',
                    'level': 'DEBUG',
                    'formatter': 'simple',
                    'stream': 'ext://sys.stdout'
                }
            },
            'loggers': {
                'root': {
                    'level': 'DEBUG',
                    'handlers': ['console']
                }
            }
        }


class KawaLogManager:
    def __init__(self,
                 dict_logging_config: dict,
                 job_log_level: int,
                 job_log_formatter):
        self.dict_logging_config = dict_logging_config
        self.job_log_level = job_log_level
        self.job_log_formatter = job_log_formatter
        self.queue = self._create_queue_and_start_logger_thread()
        self._configure_common_root_logger()
        self._configure_common_kawa_logger()

    def _configure_common_root_logger(self):
        if self.dict_logging_config:
            logging.config.dictConfig(self.dict_logging_config)

    def _configure_common_kawa_logger(self):
        kawa_logger = get_kawa_logger()
        # No specific configuration
        return kawa_logger

    def _create_queue_and_start_logger_thread(self):
        queue = multiprocessing.Manager().Queue(-1)
        lp = threading.Thread(target=logger_thread_function, args=(queue,))
        lp.start()
        return queue

    def configure_root_logger_of_job_process(self,
                                             job_log_file: str):
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.DEBUG)

        common_queue_handler = logging.handlers.QueueHandler(self.queue)
        common_queue_handler.setLevel(logging.DEBUG)
        root_logger.addHandler(common_queue_handler)

        # TODO how to control log level and formatter for job log file without impacting global logging: filter on logger name + level?
        job_file_handler = logging.FileHandler(job_log_file)
        job_file_handler.setLevel(self.job_log_level)
        job_file_handler.setFormatter(self.job_log_formatter)
        root_logger.addHandler(job_file_handler)

    def remove_all_handlers(self, logger):
        handlers_to_remove = logger.handlers.copy()
        for handler in handlers_to_remove:
            logger.removeHandler(handler)
