# 🚀 AI Resume Builder

A full-stack AI Resume Builder that allows users to generate professional ATS-friendly PDF resumes through a FastAPI backend and a dynamic JavaScript frontend.

The project focuses on demonstrating backend engineering skills including API development, validation, security, rate limiting, PDF generation, logging, and clean architecture.

---

# ✨ Features

## Backend

- FastAPI REST API
- Pydantic v2 request validation
- Professional PDF generation using ReportLab
- Global exception handling
- Structured JSON logging
- Security middleware
- Request body size validation
- Request timeout protection
- CORS support
- IP-based Rate Limiting (SlowAPI)
- Per-email download limit (Maximum 3 resumes)
- Persistent download tracking using `users.json`
- Streaming PDF response
- Clean project architecture
- Modular service layer
- Input sanitization utilities

---

## Frontend

- Dynamic Resume Form
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
- Responsive UI

---

# 🛠 Tech Stack

### Backend

- Python
- FastAPI
- Pydantic v2
- ReportLab
- SlowAPI
- Uvicorn

### Frontend

- HTML5
- CSS3
- Vanilla JavaScript

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

# 📌 API Endpoint

### Generate Resume

```
POST /resumes/create
```

Returns

- PDF Resume

---

# 🚧 Future Improvements

- User Authentication
- Database Integration
- AI-powered Resume Suggestions
- Resume Templates
- Resume History
- Cloud Storage
- Email Verification
- Resume Analytics

---

# 👩‍💻 Author

**Shruti Shashi Bhushan Dubey**

GitHub:
https://github.com/dubeyshruti801-byte

LinkedIn:
(Add your LinkedIn profile)

---

⭐ If you found this project useful, consider giving it a star.
