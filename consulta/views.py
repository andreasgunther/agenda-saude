from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from .forms import ConsultaForm
from .models import Consulta

# View de Listagem (Nao usa forms, apenas le do model e manda para o template)
class ConsultaListView(ListView):
    model = Consulta
    template_name = "consulta/consulta_list.html"
    context_object_name = ("consultas") # Como a lista sera chamada dentro do HTML
    ordering = ["-data_horario"]

# View de Criacao (Conecta o form ao template e lida com o POST/GET)
class ConsultaCreateView(CreateView):
    model = Consulta
    form_class = ConsultaForm
    template_name = "consulta/consulta_form.html"
    success_url = reverse_lazy("consulta:lista")    # Para onde vai depois de salvar com sucesso

# View de edicao (Reutiliza o mesmo form e template, mas carrega os dados existentes)
class ConsultaUpdateView(UpdateView):
    model = Consulta
    form_class = ConsultaForm
    template_name = "consulta/consulta_form.html"
    success_url = reverse_lazy("consulta:lista")