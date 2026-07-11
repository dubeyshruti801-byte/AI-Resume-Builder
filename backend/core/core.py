from typing import Optional

def api_envelope(success: bool, message: str = "", data: dict | None = None) -> dict:
    return {
        "success": success,
        "message": message,
        "data": data or {}
    }