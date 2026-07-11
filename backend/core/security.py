import json
from filelock import FileLock
from config import USERS_DB, USERS_DB_LOCK, MAX_FREE_DOWNLOADS
from core.logging_config import setup_logging

logger = setup_logging()

# ---------- File DB helpers (safe with file lock) ----------
def _read_users() -> dict:
    lock = FileLock(USERS_DB_LOCK, timeout=5)
    with lock:
        try:
            with open(USERS_DB, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}

def _write_users(users: dict) -> None:
    lock = FileLock(USERS_DB_LOCK, timeout=5)
    with lock:
        with open(USERS_DB, "w", encoding="utf-8") as f:
            json.dump(users, f, indent=2)

def increment_download_count(email: str) -> tuple[int, bool]:
    """
    Persistent counter by email. Returns (new_count, allowed_bool).
    """
    email = email.lower().strip()
    users = _read_users()
    entry = users.get(email, {"download_count": 0})
    current = int(entry.get("download_count", 0))
    if current >= MAX_FREE_DOWNLOADS:
        users[email] = entry
        _write_users(users)
        return current, False

    entry["download_count"] = current + 1
    users[email] = entry
    _write_users(users)
    return entry["download_count"], True

# ---------- SWAP WITH REDIS ----------
# For scale, replace the above with Redis:
#  - INCR a key like f"resume:downloads:{email}"
#  - Check the value > MAX_FREE_DOWNLOADS
#  - Optionally set expiry or keep permanent
# This avoids file locks and works across processes/instances.
