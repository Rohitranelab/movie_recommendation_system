import logging
import os
import sys
from datetime import datetime
from logging.handlers import RotatingFileHandler

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_DIR = "logs"

MAX_LOG_SIZE = 5 * 1024 * 1024
BACKUP_COUNT = 3


def configure_logger():

    logger = logging.getLogger()

    # Prevent duplicate handlers
    if logger.hasHandlers():
        logger.handlers.clear()

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s | %(filename)s | %(message)s"
    )

    # Always print logs to console
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Create log files ONLY when not running on Vercel
    if os.getenv("VERCEL") != "1":
        os.makedirs(LOG_DIR, exist_ok=True)

        file_path = os.path.join(LOG_DIR, LOG_FILE)

        file_handler = RotatingFileHandler(
            file_path,
            maxBytes=MAX_LOG_SIZE,
            backupCount=BACKUP_COUNT
        )

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)


configure_logger()