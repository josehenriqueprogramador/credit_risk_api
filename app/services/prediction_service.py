from typing import Dict
import logging
from app.ml.predict import PredictModel, PredictionError
from app.models import Cliente, Avaliacao

logger = logging.getLogger(__name__)

class PredictionService:
    def __init__(self, model: PredictModel):
        self.model = model

    def evaluate_and_save(self, cliente_data: Dict) -> Avaliacao:
        cliente = Cliente.objects.create(**cliente_data)
        try:
            prob = self.model.predict_proba(cliente_data)
        except PredictionError as e:
            logger.exception("prediction failed")
            raise
        avaliacao = Avaliacao.objects.create(cliente=cliente, probabilidade_inadimplencia=prob)
        return avaliacao
