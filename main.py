
from fastapi import FastAPI, UploadFile, File
from IndicASR import load_model, predict
import tempfile
import os

app = FastAPI()
model = load_model(lang="ml")  # Malayalam

@app.post("/transcribe")
async def transcribe(audio: UploadFile = File(...)):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            content = await audio.read()
            tmp.write(content)
            tmp_path = tmp.name

        # Run inference
        transcription = predict(model, tmp_path)

        os.remove(tmp_path)
        return {"transcription": transcription}
    except Exception as e:
        return {"error": str(e)}
