
# Doctor Uncle ASR API - Final Local Version

This version runs a local copy of IndicASR (mocked) and works 100% offline from GitHub.

- `main.py`: FastAPI app
- `IndicASR/`: Local model
- `requirements.txt`: Dependencies
- `runtime.txt`: Python 3.10

### Render Deployment
- Build command: pip install -r requirements.txt
- Start command: uvicorn main:app --host 0.0.0.0 --port 10000
