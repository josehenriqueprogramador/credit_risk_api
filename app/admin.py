from django.contrib import admin
from .models import Cliente, Avaliacao

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "idade", "renda_mensal")

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ("id", "cliente", "probabilidade_inadimplencia", "criado_em")
