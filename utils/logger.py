import os
import logging
from utils.constants import config
from datetime import datetime as dt

logger = logging.getLogger(__name__)

LOG_FILE = f'{config["LOG_DIR"]}/{dt.now().strftime("%Y-%m-%d")}.log'
LOG_FORMAT = "{:<19s} [{:^12s}] [{:^6s}] {:s}"


class Logger:
    def __init__(self) -> None:
        self.logfile = LOG_FILE
        # Create the directory if it doesn't exist
        if not os.path.exists(config['LOG_DIR']):
            os.makedirs(config['LOG_DIR'])
        # Open the file in append mode (creating it if it doesn't exist)
        with open(self.logfile, mode="a+") as file:
            file.close()
        self.log(msg="Application Log Initialized!")
        
    
    def log(self, msg: str, level: str = "INFO", host: str = "LocalHost"):
        with open(self.logfile, mode="a+") as lgfile:
            lgfile.write(
                LOG_FORMAT.format(
                    dt.now().strftime(config["DATETIME_FORMAT_FULL"]),
                    host,
                    level,
                    msg + '\n',
                )
            )
            lgfile.close()
