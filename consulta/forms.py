from django import forms
from django.utils import timezone
from .models import Consulta, ConsultaProcedimento, Procedimento

# Meu ModelForm
class ConsultaForm(forms.ModelForm):
    # Campo extra no formulario para selecionar os procedimentos
    procedimentos = forms.ModelMultipleChoiceField(
        queryset=Procedimento.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-check-input"}),
        required=False,
        label="Procedimentos",
    )

    class Meta:
        model = Consulta
        fields = [
            "paciente",
            "medico",
            "data_horario",
            "local_atendiemento",
            "status",
            "motivo",
            "observacoes_medicas",
        ]

        widgets = {
            "paciente": forms.Select(attrs={"class": "form-select"}),
            "medico": forms.Select(attrs={"class": "form-select"}),
            "data_horario": forms.DateTimeInput(
                attrs = {
                    "class": "form-control",
                    "type": "datetime-local",   # Habilito o selector nativo de data e hora do navegador
                },
                format="%Y-%m-%dT%H:%M",
            ),
            "local_atendimento": forms.TextInput(
                attrs = {
                    "class": "form-control",
                    "placeholder": "Ex: UBS Central, Posto Bairro Norte",
                }
            ),
            "status": forms.Select(attrs={"class": "form-select"}),
            "motivo": forms.TextInput(
                attrs = {
                    "class": "form-control",
                    "placeholder": "Queixa principal do paciente",
                }
            ),
            "observacoes_medicas": forms.Textarea(
                attrs = {
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Anotações adicionais",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Se estiver editando uma consulta existente, pre-carrega os procedimentos ja vinculados
        if self.instance and self.instance.pk:
            self.fields["procedimentos"].initial = (self.instance.procedimentos.all())

    def save(self, commit=True):
        # Salva a consulta primeiro para garantir que ela tenha um ID no banco
        consulta = super().save(commit=commit)

        if commit:
            self.save_procedimentos(consulta)

        return consulta

    def save_procedimentos(self, consulta):
        # Salva a relacao ManyToMany na tabela intermediaria personalizada
        procedimentos_selecionados = self.cleaned_data.get("procedimentos", [])

        # Remove procedimentos que foram desselecionados
        ConsultaProcedimento.objects.filter(consulta=consulta).exclude(
            procedimento__in=procedimentos_selecionados
        ).delete()

        # Adiciona novos procedimentos que ainda nao constavam
        for proc in procedimentos_selecionados:
            ConsultaProcedimento.objects.get_or_create(
                consulta=consulta,
                procedimento=proc,
                defaults={"criado_em": timezone.now()},
            )