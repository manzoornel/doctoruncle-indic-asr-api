
# Doctor Uncle Indic Conformer ASR API (Self-Contained)

This is a local, self-contained FastAPI deployment for Malayalam speech-to-text using Indic Conformer model.

## Deploy on Render

- Python version: 3.10 (runtime.txt included)
- Build command: pip install -r requirements.txt
- Start command: uvicorn main:app --host 0.0.0.0 --port 10000

NOTE: This version does not clone IndicASR from GitHub — it includes the module locally.
