from fastapi import APIRouter, Request , status
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, EmailStr, validator
from typing import List, Optional
from datetime import datetime
from core.download_limit import increment_download_count
import re
import logging

# ✅ Imports fixed for new folder structure
from core.exceptions import AppException
from core.rate_limit import limiter   # keep commented if causing issues
from services.pdf_service import PdfService
from utilities.sanitizer import sanitize_data

# -------------------------
# 🔹 Router Initialization
# -------------------------
router = APIRouter()
logger = logging.getLogger(__name__)


# -------------------------
# 🔹 Pydantic Models
# -------------------------
class Experience(BaseModel):
    title: str
    company: str
    start: str
    end: Optional[str] = None
    description: Optional[str] = None

    # ✅ Custom validation: ensure end >= start
    @validator("end")
    def check_dates(cls, v, values):
        if v and "start" in values:
            try:
                start_date = datetime.strptime(values["start"], "%Y-%m-%d")
                end_date = datetime.strptime(v, "%Y-%m-%d")
                if end_date < start_date:
                    raise ValueError("End date must be after start date")
            except ValueError:
                raise ValueError("Dates must follow YYYY-MM-DD format")
        return v

    class Config:
        schema_extra = {
            "example": {
                "title": "Developer",
                "company": "OpenAI",
                "start": "2023-01-01",
                "end": "2025-01-01",
                "description": "Worked on AI projects and backend systems."
            }
        }


class Education(BaseModel):
    degree: str
    institution: str
    year: str

    class Config:
        schema_extra = {
            "example": {
                "degree": "BCA",
                "institution": "XYZ College",
                "year": "2027"
            }
        }

class Project(BaseModel):
    title: str
    description: str
    technologies: List[str] = []

    class Config:
        schema_extra = {
            "example": {
                "title": "AI Resume Builder",
                "description": "Generates ATS-friendly resumes using AI.",
                "technologies": ["Python", "FastAPI", "ReportLab"]
            }
        }

class Certification(BaseModel):
    name: str
    issuer: str
    year: str

    class Config:
        schema_extra = {
            "example": {
                "name": "Python Essentials",
                "issuer": "Cisco",
                "year": "2025"
            }
        }
class Language(BaseModel):
    name: str
    proficiency: str

    class Config:
        schema_extra = {
            "example": {
                "name": "English",
                "proficiency": "Professional"
            }
        }

class ResumePayload(BaseModel):
    name: str
    email: EmailStr
    phone: str
    summary: Optional[str] = None
    skills: List[str] = []
    experience: List[Experience] = []
    education: List[Education] = []
    projects: List[Project] = []
    certifications: List[Certification] = []
    languages: List[Language] = []
    linkedin: Optional[str] = None
    github: Optional[str] = None
    portfolio: Optional[str] = None

    # ✅ Validate phone number (simple rule: only digits, 7–15 long)
    @validator("phone")
    def validate_phone(cls, v):
        if not re.fullmatch(r"^\+?\d{7,15}$", v):
            raise ValueError("Phone must be 7–15 digits (optionally starting with +)")
        return v

    class Config:
        schema_extra = {
            "example": {
                "name": "Shruti Dubey",
                "email": "shruti@example.com",
                "phone": "+919876543210",
                "summary": "Aspiring AI founder skilled in Python, C++, and FastAPI.",
                "skills": ["Python", "C++", "FastAPI"],
                "experience": [
                    {
                        "title": "Developer",
                        "company": "OpenAI",
                        "start": "2023-01-01",
                        "end": "2025-01-01",
                        "description": "Worked on AI projects and backend systems."
                    }
                ],
                "education": [
                    {
                        "degree": "BCA",
                        "institution": "XYZ College",
                        "year": "2027"
                    }
                ]
            }
        }


# -------------------------
# 🔹 Route
# -------------------------
@router.post(
    "/create",
    summary="Create Resume PDF",
    description="Send resume data in JSON format and get a generated PDF.",
    status_code=status.HTTP_200_OK,
    responses={
        200: {
            "content": {"application/pdf": {}},
            "description": "A generated PDF file containing the resume."
        },
        400: {"description": "Validation Error"}
    },
)
@limiter.limit("5/minute")
async def create_resume(request: Request, payload: ResumePayload):
    """
    Create resume PDF from sanitized data
    """
    logger.info("🚀 Starting resume creation...")

    sanitized_data = sanitize_data(payload.dict())

    # ✅ Validate name
    if not sanitized_data["name"]:
        raise AppException(400, "Name is required")
    
    # Download limit
    count, allowed = increment_download_count(payload.email)
    print("Route called")
    print("Email:", payload.email)
    if not allowed:
        raise AppException(
            429,
            "You have reached the maximum limit of 3 resume downloads."
        )

    # ✅ Generate PDF using PdfService
    pdf_buffer = PdfService.generate_resume_pdf(sanitized_data)
    filename = f"{sanitized_data['name'].replace(' ', '_')}_resume.pdf"

    logger.info("✅ PDF ready for download: %s", filename)

    return StreamingResponse(
        pdf_buffer,
        media_type="application/pdf",
        headers={"Content-Disposition": f"attachment; filename={filename}"},
    )
