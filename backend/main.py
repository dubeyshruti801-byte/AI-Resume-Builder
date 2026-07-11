from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi.errors import RateLimitExceeded
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from config import APP_NAME
from core.logging_config import setup_logging
from core.rate_limit import limiter, rate_limit_exceeded_handler
from core.exceptions import AppException, global_exception_handler
from core.middlewares import security_and_limits

# ✅ Import your router correctly (resumes.py file)
from api.routes.resumes import router as resumes_router

from fastapi.openapi.utils import get_openapi
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html

# Logging
logger = setup_logging()

# ✅ Create FastAPI app first
app = FastAPI(
    title=APP_NAME,
    version="0.1.0",
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.state.limiter = limiter

# ✅ CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # TODO: restrict in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.middleware("http")(security_and_limits)

# ✅ Register routers (AFTER app is defined)
app.include_router(resumes_router, prefix="/resumes", tags=["Resumes"])

# ✅ Exception handlers
app.add_exception_handler(RateLimitExceeded, rate_limit_exceeded_handler)

@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException):
    logger.error(exc.message)
    return exc.to_response()

app.add_exception_handler(Exception, global_exception_handler)

# ✅ Root endpoint
@app.get("/")
async def root():
    return {"success": True, "message": f"{APP_NAME} is running 🚀"}

