from django.contrib import admin
from .models import Consulta, Procedimento

# Register your models here
@admin.register(Procedimento)
class ProcedimentoAdmin(admin.ModelAdmin):
    list_display = ("nome", "descricao")
    search_fields = ("nome",)

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = (
        "paciente",
        "medico",
        "data_horario",
        "status",    
    )

    list_filter = ("status", "local_atendimento", "data_horario", "medico")
    search_fields = (
        "paciente_nome",
        "medico_nome",
        "paciente_cpf",
        "local_atendimento"
    )

    # Deixa o ManyToMany melhor de selecionar com duas caixas lado a lado
    filter_horizontal = ("procedimentos",)