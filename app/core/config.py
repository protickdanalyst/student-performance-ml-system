from pydantic import BaseSettings

class Settings(BaseSettings):
    MODEL_NAME: str = "my_model"
    MODEL_VERSION: str = "v1"
    MLFLOW_TRACKING_URI: str = "http://mlflow:5000"
    DATABASE_URL: str = "sqlite:///./test.db"

    class Config:
        env_file = ".env"

settings = Settings()