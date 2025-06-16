from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel

MODEL_PATH = Path(__file__).resolve().parents[2] / "model.joblib"

app = FastAPI(title="Retail Forecast API")


class PredictionRequest(BaseModel):
    store: int
    sku: int


@app.on_event("startup")
def load_model() -> None:
    import joblib
    global model
    model = joblib.load(MODEL_PATH)


@app.post("/predict")
def predict(req: PredictionRequest) -> dict:
    pred = model.predict([[req.store, req.sku]])[0]
    return {"prediction": float(pred)}
