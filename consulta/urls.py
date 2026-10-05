from django.urls import path
from . import views

# app_name define o namespace para usar no template: {% url 'consulta:lista' %}
app_name = "consulta"

urlpatterns = [
    # Listagem de consultas
    path("", views.ConsultaListView.as_view(), name="lista"),
    # Agendar nova consulta
    path("nova/", views.ConsultaCreateView.as_view(), name="nova"),
    # Editar consulta existente (espera a primary key / ID na URL)
    path("<int:pk>/editar/", views.ConsultaUpdateView.as_view(), name="editar"),
]

