from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class RegistroCovid(models.Model):
	responsavel_pelo_preenchimento = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
	data_anexo = models.DateField(auto_now_add=True)
	hora_anexo = models.TimeField(auto_now_add=True)
	nome_solicitante = models.CharField(max_length=100, blank=True, default='', null=True)
	nome_paciente = models.CharField(max_length=100, blank=True, default='', null=True)
	unidade_origem = models.CharField(max_length=100, blank=True, default='', null=True)
	idade_paciente = models.IntegerField(blank=True, null=True)
	recurso_que_precisa = models.TextField()
	cidade_origem = models.CharField(max_length=50, blank=True, default='')
	telefone_retorno = models.CharField(max_length=30, blank=True, default='', null=True)
	frequencia_respiratoria = models.IntegerField(blank=True, null=True)
	saturacao = models.IntegerField(blank=True, null=True)
	ar_o2 = models.CharField(max_length=100, blank=True, default='', null=True)
	frequencia_cardiaca = models.IntegerField(blank=True, null=True)
	pa = models.CharField(max_length=11, default='', null=True)
	conciencia = models.CharField(max_length=100, blank=True, default='', null=True)
	temperatura = models.FloatField(blank=True, null=True)
	codigo_registro = models.CharField(max_length=100, default='', null=True)
	observacoes = models.TextField(blank=True, default='', null=True)

	sindrome_gripal = ArrayField(models.CharField(max_length=20), blank=True, null=True)
	tempo_quadro_sintomatico = models.IntegerField(blank=True, null=True)
	exposicao_pessoa_infectada = models.CharField(max_length=5, blank=True, null=True)
	parentesco = models.CharField(max_length=30, blank=True, null=True)
	comorbidades = ArrayField(models.CharField(max_length=100), blank=True, null=True)
	outras_cardiopatias = models.CharField(max_length=100, blank=True, null=True)
	idade_gestacional = models.CharField(max_length=100, blank=True, null=True)
	comorbidades_obstetricas = models.CharField(max_length=100, blank=True, null=True)
	gesta_para = models.CharField(max_length=100, blank=True, null=True)
	




	def __str__(self):
		return str(self.descricao)