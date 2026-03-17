from sqlalchemy import Column, Integer, Float, JSON, String
from app.db.database import Base

class PredictionLog(Base):
    __tablename__ = "predictions"
    id = Column(Integer, primary_key=True)
    input_data = Column(JSON)
    prediction = Column(Float)
    model_version = Column(String)