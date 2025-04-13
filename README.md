
# Indic Conformer ASR API (Malayalam)

This is a FastAPI backend using AI4Bharat's Indic Conformer ASR model for Malayalam speech-to-text conversion.

## API Endpoint

POST /transcribe

### Request:
- Multipart/form-data
- Field: "audio" (.wav file)

### Response:
- JSON with transcription in Malayalam Unicode

## Deploy Instructions (Render.com)
1. Upload to GitHub
2. Create new Web Service on https://render.com
3. Use:
   - Python version: 3.10+
   - Build command: `pip install -r requirements.txt`
   - Start command: `uvicorn main:app --host 0.0.0.0 --port 10000`
