from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    idade = models.PositiveSmallIntegerField()
    renda_mensal = models.DecimalField(max_digits=12, decimal_places=2)
    historico_credito = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return f"{self.nome} ({self.id})"

class Avaliacao(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="avaliacoes")
    probabilidade_inadimplencia = models.FloatField()
    criado_em = models.DateTimeField(auto_now_add=True)
