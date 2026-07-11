import asyncio
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette import status
from config import REQUEST_TIMEOUT_SECONDS, MAX_BODY_SIZE_BYTES
from core.logging_config import setup_logging

logger = setup_logging()

SECURITY_HEADERS = {
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "DENY",
    "Referrer-Policy": "no-referrer",
    "Content-Security-Policy": "default-src 'self' 'unsafe-inline' data:",
}

async def security_and_limits(request: Request, call_next):
    cl = request.headers.get("content-length")
    if cl:
        try:
            if int(cl) > MAX_BODY_SIZE_BYTES:
                logger.warning("payload_too_large", extra={"content_length": cl})
                return JSONResponse(
                    {"success": False, "message": "Request body too large"},
                    status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
                )
        except ValueError:
            pass

    try:
        response = await asyncio.wait_for(call_next(request), timeout=REQUEST_TIMEOUT_SECONDS)
    except asyncio.TimeoutError:
        logger.error("request_timeout", extra={"path": str(request.url)})
        return JSONResponse(
            {"success": False, "message": "Request timed out"},
            status_code=status.HTTP_504_GATEWAY_TIMEOUT,
        )

    # Don't apply CSP to FastAPI documentation
    if request.url.path not in ("/docs", "/redoc", "/openapi.json"):

        for k, v in SECURITY_HEADERS.items():
            response.headers[k] = v
    return response
