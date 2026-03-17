from fastapi import FastAPI
from app.api.routes import predict, health, metrics
from app.models.model_registry import ModelRegistry
from app.services.prediction_service import PredictionService

app = FastAPI()

model = None
service = None

@app.on_event("startup")
def startup():
    global model, service
    registry = ModelRegistry()
    model = registry.load_model()
    service = PredictionService(model)

app.include_router(predict.router, prefix="/predict")
app.include_router(health.router, prefix="/health")
app.include_router(metrics.router, prefix="/metrics")