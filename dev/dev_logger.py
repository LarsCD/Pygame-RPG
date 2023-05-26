import logging
from datetime import datetime

time_start = datetime.today()

logger_enabled = True

class DevLogger:
    def __init__(self, logging_class, log_level=logging.DEBUG, print_level=logging.DEBUG):
        self.logger_enabled = logger_enabled
        # logging details
        logging.basicConfig(level=print_level)
        logger_name = str(logging_class.__name__)
        log_file_path = str(f"dev/logs/dev-log-{time_start.date()}-{time_start.time().hour}h-{time_start.time().minute}m-{time_start.time().second}s.txt")

        self.logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setLevel(level=log_level)
        formatter = logging.Formatter("[%(asctime)s]: %(levelname)s: %(name)s: %(message)s")
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)


    def log(self, level, message):
        if self.logger_enabled:
            self.logger.log(level, message)