from pydantic import BaseModel

class PredictionRequest(BaseModel):
    conversation: str

class PredictionResponse(BaseModel):
    summary: str
    prescription: dict

class TranscriptionRequest(BaseModel):
    url: str

class TranscriptionResponse(BaseModel):
    text: str