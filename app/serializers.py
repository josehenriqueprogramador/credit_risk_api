from rest_framework import serializers
from .models import Cliente, Avaliacao

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ("id", "nome", "idade", "renda_mensal", "historico_credito")

class AvaliacaoSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(read_only=True)

    class Meta:
        model = Avaliacao
        fields = ("id", "cliente", "probabilidade_inadimplencia", "criado_em")
