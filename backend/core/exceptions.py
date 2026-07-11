from fastapi import Request
from fastapi.responses import JSONResponse
from starlette import status
from core.logging_config import setup_logging

logger = setup_logging()


def json_error(message: str, code: int, data: dict | None = None) -> JSONResponse:
    return JSONResponse(
        status_code=code,
        content={"success": False, "message": message, "data": data or {}},
    )


async def global_exception_handler(request: Request, exc: Exception):
    logger.exception("unhandled_exception", extra={"path": str(request.url)})
    return json_error("Unexpected server error", status.HTTP_500_INTERNAL_SERVER_ERROR)


# ✅ Add this AppException class
class AppException(Exception):
    """Custom application exception with status code and message."""

    def __init__(self, status_code: int, message: str, data: dict | None = None):
        self.status_code = status_code
        self.message = message
        self.data = data or {}
        super().__init__(message)

    def to_response(self) -> JSONResponse:
        """Convert exception to JSON response directly."""
        return json_error(self.message, self.status_code, self.data)
