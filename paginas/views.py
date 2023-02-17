from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

# A classe PaginaInicial "Extends" TemplateView
class PaginaInicial(TemplateView):
    # Toda classe Filha do TemplateView precisa do 
    # atributo abaixo para definir um template a ser renderizado
    template_name = 'paginas/home.html'

class SobreView(TemplateView):
    template_name = 'paginas/about.html'

class ContatoView(TemplateView):
    template_name = 'paginas/contact.html'