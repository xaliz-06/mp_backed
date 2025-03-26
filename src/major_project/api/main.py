from fastapi import FastAPI
from src.major_project.api.routes import predictions, transcripts,health
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Major Project")
app.include_router(predictions.router)
app.include_router(health.router)
app.include_router(transcripts.router)