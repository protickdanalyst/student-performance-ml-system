import pandas as pd

class PredictionService:
    def __init__(self, model):
        self.model = model

    def predict(self, data: dict):
        df = pd.DataFrame([data])
        return float(self.model.predict(df)[0])