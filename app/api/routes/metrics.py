from fastapi import APIRouter
from app.monitoring.metrics import get_metrics

router = APIRouter()

@router.get("/")
def metrics():
    return get_metrics()