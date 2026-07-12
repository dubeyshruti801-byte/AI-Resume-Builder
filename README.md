# 🚀 AI Resume Builder

A full-stack AI Resume Builder that allows users to generate professional ATS-friendly PDF resumes through a FastAPI backend and a dynamic JavaScript frontend.

The project focuses on demonstrating backend engineering skills including API development, validation, security, rate limiting, PDF generation, logging, and clean architecture.

---

---

# 🌐 Live Demo

### Frontend (Vercel)

https://ai-resume-builder-henna-three.vercel.app/

### Backend API (Render)

https://ai-resume-builder-backend-gjd1.onrender.com

### Swagger Documentation

https://ai-resume-builder-backend-gjd1.onrender.com/docs

# ✨ Features

## Backend

- RESTful API built with FastAPI
- Pydantic v2 request validation
- Professional ATS-friendly PDF generation
- Streaming PDF responses
- Global exception handling
- Structured JSON logging
- Modular project architecture
- Security middleware
- Request timeout protection
- Request body size validation
- Input sanitization
- IP-based rate limiting (SlowAPI)
- Per-email download limit (3 downloads)
- Persistent download tracking using users.json
- CORS configuration
---

## Frontend

- Responsive user interface
- Dynamic resume sections
- Add/Remove Skills
- Add/Remove Experience
- Add/Remove Education
- Add/Remove Projects
- Add/Remove Certifications
- Add/Remove Languages
- Client-side validation
- Loading overlay
- Toast notifications
- Automatic PDF download
- Clear Form functionality

---

# 🛠 Tech Stack

## Backend

- Python
- FastAPI
- Pydantic v2
- ReportLab
- SlowAPI
- Uvicorn

## Frontend

- HTML5
- CSS3
- Vanilla JavaScript

## Deployment

- Render
- Vercel

## Version Control

- Git
- GitHub

---

# 📁 Project Structure

```
AI-Resume-Builder/

├── backend/
│   ├── api/
│   ├── core/
│   ├── services/
│   ├── utilities/
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── css/
│   ├── js/
│   └── index.html
│
├── README.md
├── LICENSE
└── .gitignore
```

---

---

# 🏗 Architecture
 User
   │
   ▼
Frontend (Vercel)
   │
   ▼
FastAPI Backend (Render)
   │
   ▼
Validation
(Pydantic)
   │
   ▼
PDF Generator
(ReportLab)
   │
   ▼
Resume PDF

# 📄 Resume Sections Supported

- Personal Information
- Professional Summary
- Skills
- Experience
- Projects
- Certifications
- Languages
- Education

The generated PDF also contains:

- Clickable Email
- LinkedIn Profile
- GitHub Profile
- Portfolio Link

---

# 🔒 Security Features

- Request Validation
- Input Sanitization
- Global Exception Handling
- Rate Limiting
- Download Limiting
- Security Headers
- Request Timeout Protection

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/dubeyshruti801-byte/AI-Resume-Builder.git
```

Go inside the backend folder

```bash
cd AI-Resume-Builder/backend
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file if required for your environment.

(Current version does not require environment variables.)

Run the server

```bash
uvicorn main:app --reload
```

The backend will start at

```
http://127.0.0.1:8000
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

---

# 🚀 Deployment

Frontend is deployed on **Vercel**

Backend is deployed on **Render**

Both services are automatically redeployed whenever changes are pushed to the GitHub repository.

# 📌 API Endpoint

### Generate Resume

```
POST /resumes/create
```

Returns

- application/pdf

---

# 🚧 Future Improvements

- User Authentication (JWT)
- Database Integration (PostgreSQL)
- AI-powered Resume Suggestions
- Multiple Resume Templates
- Resume History
- Resume Versioning
- Cloud Storage
- Email Verification
- Resume Analytics Dashboard
- Admin Dashboard

---

# 💡 Skills Demonstrated

- Backend API Development
- REST API Design
- FastAPI
- Pydantic Validation
- ReportLab PDF Generation
- Frontend Development
- DOM Manipulation
- Error Handling
- Security Best Practices
- Rate Limiting
- File Handling
- Deployment
- Git & GitHub
---

# 👩‍💻 Author

**Shruti Shashi Bhushan Dubey**

GitHub

https://github.com/dubeyshruti801-byte

LinkedIn

https://www.linkedin.com/in/shruti-dubey-a1853b353/

---

# 📜 License

This project is licensed under the MIT License.


---

⭐ If you found this project useful, consider giving it a star.
