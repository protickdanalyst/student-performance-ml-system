from fastapi import APIRouter, Depends
from app.schemas.prediction_schema import PredictionRequest
from app.services.prediction_service import PredictionService
from app.db.database import SessionLocal
from app.db.models import PredictionLog
from app.monitoring.metrics import record
import time

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

service_instance = None

def get_service():
    return service_instance

@router.post("/")
def predict(req: PredictionRequest, db=Depends(get_db)):
    start = time.time()
    success = True
    try:
        result = service_instance.predict(req.dict())
        db.add(PredictionLog(
            input_data=req.dict(),
            prediction=result,
            model_version="v1"
        ))
        db.commit()
        return {"prediction": result}
    except Exception as e:
        success = False
        return {"error": str(e)}
    finally:
        record(time.time() - start, success)