import pytest
from rest_framework.test import APIClient
from django.urls import reverse

@pytest.mark.django_db
def test_create_evaluation(monkeypatch):
    client = APIClient()
    url = "/api/avaliacoes/"
    data = {"nome": "João", "idade": 35, "renda_mensal": "5000.00", "historico_credito": 2}

    # monkeypatch the PredictModel to return fixed probability
    class Dummy:
        def predict_proba(self, d):
            return [[0.3, 0.7]]

    # patch the service's model
    import importlib
    vm = importlib.import_module("app.views")
    vm.service = vm.PredictionService(Dummy())

    resp = client.post(url, data, format="json")
    assert resp.status_code == 201
    assert "probabilidade_inadimplencia" in resp.data or "probabilidade_inadimplencia" in resp.data.keys() or "probabilidade_inadimplencia" in str(resp.data)
