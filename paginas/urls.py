from django.urls import path
from .views import PaginaInicial, SobreView, ContatoView

urlpatterns = [
    path('', PaginaInicial.as_view(), name="home"),
    path('sobre/', SobreView.as_view(), name='about'),
    path('contato/', ContatoView.as_view(), name='contact'),
]
