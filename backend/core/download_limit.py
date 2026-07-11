import json
from pathlib import Path

# -------------------------
# Configuration
# -------------------------

MAX_DOWNLOADS = 3

USERS_FILE = Path("users.json")


# -------------------------
# Load users
# -------------------------

def load_users() -> dict:
    """
    Load all users from users.json.

    Returns:
        {
            "abc@gmail.com": 2,
            "xyz@gmail.com": 1
        }
    """

    if not USERS_FILE.exists():
        return {}

    with open(USERS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


# -------------------------
# Save users
# -------------------------

def save_users(users: dict) -> None:
    """
    Save updated user counts into users.json.
    """
    
    
    with open(USERS_FILE, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4)


# -------------------------
# Increment Download Count
# -------------------------

def increment_download_count(email: str):
    """
    Increase resume download count.

    Returns
    -------
    count   -> current download count
    allowed -> True/False
    """
    print("increment_download_count called")
    print("Email:", email)


    users = load_users()

    current_count = users.get(email, 0)

    if current_count >= MAX_DOWNLOADS:
        return current_count, False

    current_count += 1

    users[email] = current_count

   


    save_users(users)


    return current_count, True