from django.contrib import admin
from .models import Medico, Paciente

# Register your models here
@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    # Colunas visiveis na tabela de listagem
    list_display = ("nome", "crm", "especialidade", "telefone", "email")

    # Campos que terao barra de busca no topo
    search_fields = ("nome", "crm", "especialidade")

    # Filtros laterais
    list_filter = ("especialidade",)

    # Ordenacao padrao
    ordering = ("nome",)

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    # Colunas visiveis na listagem
    list_display = ("nome", "cpf", "cartao_sus", "telefone", "data_nascimento")

    # Barra de busca
    search_fields = ("nome", "cpf", "cartao_sus")

    # Ordenacao padrao por nome
    ordering = ("nome",)