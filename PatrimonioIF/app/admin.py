from django.contrib import admin
from .models import Unidade, Predio
from .forms import PredioForm
from app.models import *
# Register your models here.
admin.site.register(Funcao)
admin.site.register(Permissao)
admin.site.register(Colaborador)
admin.site.register(Sala)
admin.site.register(Tipo)
admin.site.register(Patrimonio)
admin.site.register(Alocacao)

class PredioInline(admin.TabularInline):  
    model = Predio
    form = PredioForm
    extra = 1  # numero de formularios vazios a serem exibidos

class UnidadeAdmin(admin.ModelAdmin):
    inlines = [PredioInline]

admin.site.register(Unidade, UnidadeAdmin),