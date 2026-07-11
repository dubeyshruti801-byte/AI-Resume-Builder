# AI Resume Builder Backend

Features:
- Robust exception handling + global error handlers
- File handling with **safe persistent download counters** (`users.json` + file lock)
- Structured, rotating log file (JSON logs)
- Pydantic v2 validation with helpful messages
- Security headers, CORS, body-size check
- Request timeout guard
- Rate limiting (IP-level via slowapi) **and** 3-downloads-per-email counter
- Streaming PDF download with professional layout + filename
- Consistent JSON envelope
- Clear comments on swapping file DB for Redis

## Run
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
uvicorn main:app --reload
