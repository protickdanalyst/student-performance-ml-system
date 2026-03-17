import mlflow.pyfunc
from app.core.config import settings

class ModelRegistry:
    def __init__(self):
        mlflow.set_tracking_uri(settings.MLFLOW_TRACKING_URI)

    def load_model(self):
        return mlflow.pyfunc.load_model(
            f"models:/{settings.MODEL_NAME}/{settings.MODEL_VERSION}"
        )