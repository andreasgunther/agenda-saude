from django.db import models

class Pessoa(models.Model):
    # Classe base abstrata para compartilhar campos comuns
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True, verbose_name="Endereço/Bairro")

    class Meta:
        abstract = (True) # O Django nao criara uma tabela 'Pessoa', apenas reutilizara os campos

    def __str__(self):
        return self.nome


class Medico(Pessoa):
    crm = models.CharField(max_length=20, unique=True, verbose_name="CRM Registro")
    especialidade = models.CharField(max_length=100, help_text="Ex: Clínico Geral, Pediatra, Cardiologista")

    class Meta:
        verbose_name = "Médico"
        verbose_name_plural = "Médicos"


class Paciente(Pessoa):
    cpf = models.CharField(max_length=14, unique=True, blank=True, null=True, verbose_name="CPF")
    cartao_sus = models.CharField(max_length=20, blank=True, null=True, verbose_name="Cartão Nacional de Saúde (SUS)")
    data_nascimento = models.DateField(blank=True, null=True, verbose_name="Data de Nascimento")
    observacoes = models.TextField(blank=True, null=True, help_text="Alergias, condições prévias ou histórico")

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"