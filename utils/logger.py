import logging
from utils.constants import config
from datetime import datetime as dt

logger = logging.getLogger(__name__)

LOG_FILE = f'{config["LOG_DIR"]}/{dt.now().strftime("%Y-%m-%d")}-log.txt'
LOG_FORMAT = "{:<19s} [{:^6s}] {:s}"


class Logger:
    def __init__(self) -> None:
        self.logfile = LOG_FILE
        self.log(msg="Application Log Initialized")

    def log(self, msg: str, level: str = "INFO"):
        with open(self.logfile, mode="w") as lgfile:
            lgfile.write(
                LOG_FORMAT.format(
                    dt.now().strftime(config["DATETIME_FORMAT_FULL"]),
                    level,
                    msg,
                )
            )
