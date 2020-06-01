from django.contrib import admin
from .models import RegistroCovid

# Register your models here.

@admin.register(RegistroCovid)
class RegistroCovidAdmin(admin.ModelAdmin):
	list_display = ['codigo_registro', 'nome_solicitante', 'estabelecimento_solicitante']