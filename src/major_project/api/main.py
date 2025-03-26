from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.major_project import Predictor, load_dummy_data

app = FastAPI(title="Major Project")

class PredictionRequest(BaseModel):
    conversation: str

class PredictionResponse(BaseModel):
    summary: str
    prescription: dict

predictor = Predictor()

@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    try:
        predicted_class, tokens = predictor.generate_predicted_class_and_tokens(input_txt=request.conversation)

        prescription = predictor.generate_prescription(
            tokens=tokens,
            input_txt=request.conversation,
            predicted_class=predicted_class
        )

        if prescription:
            summary_text = f"This prescription includes medications like {', '.join(prescription.get('Medicines', ['None']))}. Recommended tests are {', '.join(prescription.get('Tests', ['None']))}. Key advice is {', '.join(prescription.get('Advice', ['None']))}. Ensure to follow the dosage and duration carefully and seek follow-up if symptoms persist."
        else:
            summary_text = "No relevant prescription information extracted from the provided text."

        return {
            "summary": summary_text,
            "prescription": prescription
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 