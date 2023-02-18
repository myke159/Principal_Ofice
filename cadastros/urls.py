from django.urls import path
from .views import CampoCreate, AtividadeCreate
from .views import CampoUpdate, AtividadeUpdate
from .views import CampoDelete, AtividadeDelete
from .views import CampoList, AtividadeList

urlpatterns = [
    # Create
    path('cadastrar/campo/', CampoCreate.as_view(), name="cadastrar-campo"),
    path('cadastrar/atividade/', AtividadeCreate.as_view(), name="cadastrar-atividade"),

    # Update
    path('editar/campo/<int:pk>/', CampoUpdate.as_view(), name="editar-campo"),
    path('editar/atividade/<int:pk>/', AtividadeUpdate.as_view(), name="editar-atividade"),

    # Update
    path('excluir/campo/<int:pk>/', CampoDelete.as_view(), name="excluir-campo"),
    path('excluir/atividade/<int:pk>/', AtividadeDelete.as_view(), name="excluir-atividade"),

    # List
    path('listar/campos/', CampoList.as_view(), name="listar-campos"),
    path('listar/atividades/', AtividadeList.as_view(), name="listar-atividades"),
]
