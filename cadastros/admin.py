from django.contrib import admin

# Importar as classes
from .models import Campo, Atividade

# Register your models here.

@admin.register(Campo)
class RaffleModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'descricao']


@admin.register(Atividade)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'campo', 'numero', 'descricao', 'pontos', 'detalhes']