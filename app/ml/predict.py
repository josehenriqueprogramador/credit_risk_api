from typing import Dict
import pandas as pd
import joblib
import os

class PredictionError(Exception):
    pass

class PredictModel:
    def __init__(self, model_path: str = None):
        if model_path is None:
            model_path = os.path.join(os.path.dirname(__file__), "model", "model.joblib")
        self.model_path = model_path
        if not os.path.exists(self.model_path):
            raise PredictionError(f"model not found at {self.model_path}")
        self.model = joblib.load(self.model_path)

    def predict_proba(self, data: Dict) -> float:
        df = pd.DataFrame([data])
        # Ensure columns order if needed in production
        try:
            probs = self.model.predict_proba(df.values)
            # assume binary and positive class at index 1
            prob = float(probs[0][1])
            return prob
        except Exception as exc:
            raise PredictionError(exc)
