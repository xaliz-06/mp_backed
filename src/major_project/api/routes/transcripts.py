from fastapi import APIRouter, HTTPException
from src.major_project.api.schemas import TranscriptionRequest, TranscriptionResponse
import assemblyai as aai
import os

router = APIRouter(prefix="/api/v1", tags=["Transcription"])

@router.post('/transcribe', response_model=TranscriptionResponse)
async def transcribe(request: TranscriptionRequest):
    try:
        aai.settings.api_key = os.environ.get("AAI_API_KEY")
        transcriber = aai.Transcriber()
        transcript = transcriber.transcribe(request.url)

        return {
            "text": transcript.text
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 