
# Doctor Uncle Indic Conformer ASR API

This app uses AI4Bharat's Indic Conformer ASR model for Malayalam speech-to-text conversion.

## API Endpoint

POST /transcribe

### Request:
- Multipart/form-data
- Field: "audio" (.wav or .mp3)

### Response:
```json
{
  "transcription": "മലയാളം വാക്കുകൾ ഇവിടെ വരും"
}
```

## Deployment Instructions (Render)

- Python version: 3.10 (set via runtime.txt)
- Build command: pip install -r requirements.txt
- Start command: uvicorn main:app --host 0.0.0.0 --port 10000
