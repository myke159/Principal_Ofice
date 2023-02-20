from django.contrib import admin
from .models import Perfil

# Register your models here.

@admin.register(Perfil)
class PerfilModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome_completo', 'cpf', 'telefone', 'usuario']