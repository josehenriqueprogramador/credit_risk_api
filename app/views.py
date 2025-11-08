from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import ClienteSerializer, AvaliacaoSerializer
from .services.prediction_service import PredictionService
from .ml.predict import PredictModel

# In production, você usaria injeção de dependência, um factory ou container.
try:
    MODEL_PATH = None  # default path inside app/ml/model/model.joblib
    model_adapter = PredictModel(MODEL_PATH)
except Exception:
    model_adapter = None

service = PredictionService(model_adapter) if model_adapter else None

class AvaliacaoViewSet(viewsets.ViewSet):
    def create(self, request):
        if service is None:
            return Response({"detail": "Model não carregado. Rode 'make train' ou verifique logs."}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        serializer = ClienteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        avaliacao = service.evaluate_and_save(serializer.validated_data)
        out = AvaliacaoSerializer(avaliacao)
        return Response(out.data, status=status.HTTP_201_CREATED)
