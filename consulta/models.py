from django.db import models
from pessoa.models import Medico, Paciente

class Procedimento(models.Model):
    # Exames, procedimentos ou servicos medicos que podem ser vinculados a consulta
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Procedimento / Exame"
        verbose_name_plural = "Procedimentos e Exames"

    def __str__(self):
        return self.nome

class Consulta(models.Model):

    STATUS_CHOICES = (
        ("AGENDADA", "Agendada"),
        ("REALIZADA", "Realizada"),
        ("CANCELADA", "Cancelada")
    )

    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name="consultas")
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="consultas")
    data_horario = models.DateTimeField(verbose_name="Data e Horário")
    local_atendimento = models.CharField(max_length=150, help_text="Ex: UBS Centro, Posto Bairro Sul, Clínica Municipal",)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="AGENDADA")

    # Relação Many to Many
    # Uma consulta que pode envolver múltiplos procedimentos/exames
    procedimentos = models.ManyToManyField(
        Procedimento,
        related_name="consultas",
        help_text="Selecione os exames/procedimentos vinculados a esta consulta",
    )

    motivo = models.CharField(max_length=255, blank=True, null=True, verbose_name="Motivo/Queixa")
    observacoes_medicas = models.TextField(blank=True, null=True, verbose_name="Evolução / Observações")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"
        ordering = ["-data_horario"]

    def __str__(self):
        return f"{self.paciente.nome} com Dr(a). {self.medico.nome} em {self.data_horario.strftime('%d/%m/%Y %H:%M')}"