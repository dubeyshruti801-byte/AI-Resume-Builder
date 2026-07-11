import logging
import os
from logging.handlers import RotatingFileHandler
from pythonjsonlogger import jsonlogger
from config import LOG_DIR, LOG_FILE, LOG_MAX_BYTES, LOG_BACKUP_COUNT

def setup_logging() -> logging.Logger:
    os.makedirs(LOG_DIR, exist_ok=True)
    logger = logging.getLogger("resume_builder")
    logger.propagate = False
    logger.setLevel(logging.INFO)

    # Rotating file handler (JSON logs)
    file_handler = RotatingFileHandler(
        os.path.join(LOG_DIR, LOG_FILE),
        maxBytes=LOG_MAX_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding="utf-8",
    )
    formatter = jsonlogger.JsonFormatter("%(asctime)s %(levelname)s %(name)s %(message)s")
    file_handler.setFormatter(formatter)

    # Also log to stdout (useful on containers)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)
    return logger
