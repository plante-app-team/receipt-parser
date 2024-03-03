import logging
import os

LOG_FILE_NAME = "dev.log"


def set_logger():
    logger = logging.getLogger("receipt-parser")
    if os.getenv("ENV_NAME") == "dev":
        logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler(LOG_FILE_NAME)
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger
