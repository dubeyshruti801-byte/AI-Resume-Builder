import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "AI Resume Builder")
ENV = os.getenv("ENV", "development")

# Limits / guards
REQUEST_TIMEOUT_SECONDS = int(os.getenv("REQUEST_TIMEOUT_SECONDS", "20"))
MAX_BODY_SIZE_BYTES = int(os.getenv("MAX_BODY_SIZE_BYTES", "2000000"))
MAX_FREE_DOWNLOADS = int(os.getenv("MAX_FREE_DOWNLOADS", "3"))
IP_RATE_LIMIT = os.getenv("IP_RATE_LIMIT", "200/hour")

# Logging
LOG_DIR = os.getenv("LOG_DIR", "logs")
LOG_FILE = os.getenv("LOG_FILE", "app.log")
LOG_MAX_BYTES = int(os.getenv("LOG_MAX_BYTES", "1048576"))  # 1MB
LOG_BACKUP_COUNT = int(os.getenv("LOG_BACKUP_COUNT", "5"))

# Storage
USERS_DB = os.getenv("USERS_DB", "storage/users.json")
USERS_DB_LOCK = USERS_DB + ".lock"
