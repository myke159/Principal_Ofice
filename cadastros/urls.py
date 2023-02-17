from django.urls import path
from .views import CampoCreate, AtividadeCreate

urlpatterns = [
    path('cadastrar/campo/', CampoCreate.as_view(), name="cadastros-campo"),
    path('cadastrar/atividade/', AtividadeCreate.as_view(), name="cadastros-atividade"),
]
