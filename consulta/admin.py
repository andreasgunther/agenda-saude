from django.contrib import admin
from .models import Consulta, Procedimento, ConsultaProcedimento

@admin.register(Procedimento)
class ProcedimentoAdmin(admin.ModelAdmin):
    list_display = ("nome", "descricao")
    search_fields = ("nome",)

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = (
        "paciente",
        "medico",
        "data_consulta",
        "status",    
    )

    list_filter = ("status", "local_atendimento", "data_consulta", "medico")
    search_fields = (
        "paciente_nome",
        "medico_nome",
        "paciente_cpf",
        "local_atendimento"
    )

class ConsultaProcedimentoInline(admin.TabularInline):
    model = ConsultaProcedimento
    extra = 1   # Quantidade de linhas em branco exibidas

@admin.register(ConsultaProcedimento)
class ConsultaProcedimentoAdmin(admin.ModelAdmin):
    list_display = ("consulta", "procedimento", "criado_em")
    list_filter = ("criado_em", "procedimento")