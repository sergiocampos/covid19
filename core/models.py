from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class UserProfileInfo(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	#portfolio_site = models.URLField(blank=True)
	#profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

	def __str__(self):
		return self.user.username



class RegistroCovid(models.Model):
	responsavel_pelo_preenchimento = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
	data_notificacao = models.DateField(auto_now_add=True)
	hora_notificacao = models.TimeField(auto_now_add=True)
	codigo_registro_total = models.IntegerField(blank=True, null=True)
	codigo_registro_mensal = models.IntegerField(blank=True, null=True)
	codigo_registro_completo = models.CharField(max_length=100, blank=True, default='', null=True)
	nome_solicitante = models.CharField(max_length=100, blank=True, default='', null=True)
	municipio_estabelecimento_solicitante = models.CharField(max_length=100, blank=True, default='', null=True)
	estabelecimento_solicitante = models.CharField(max_length=200, blank=True, default='', null=True)
	estabelecimento_solicitante_outro = models.CharField(max_length=200, blank=True, default='', null=True)

	municipio_estabelecimento_referencia = models.CharField(max_length=100, blank=True, default='', null=True)
	estabelecimento_referencia = models.CharField(max_length=200, blank=True, default='', null=True)
	estabelecimento_referencia_outro = models.CharField(max_length=200, blank=True, default='', null=True)
	
	nome_paciente = models.CharField(max_length=100, blank=True, default='', null=True)
	idade_paciente = models.IntegerField(blank=True, null=True)
	sexo_paciente = models.CharField(max_length=10, blank=True, null=True)
	regulacao_status = ArrayField(models.CharField(max_length=100), blank=True, null=True)
	recurso_que_precisa = models.TextField(blank=True, null=True)
	estado_origem = models.CharField(max_length=100, blank=True, default='', null=True)
	cidade_origem = models.CharField(max_length=100, blank=True, default='', null=True)
	telefone_retorno = models.CharField(max_length=100, blank=True, default='', null=True)
	frequencia_respiratoria = models.IntegerField(blank=True, null=True)
	saturacao_paciente = models.IntegerField(blank=True, null=True)
	ar_o2 = models.CharField(max_length=100, blank=True, default='', null=True)
	frequencia_cardiaca = models.IntegerField(blank=True, null=True)
	pa = models.CharField(max_length=100, default='', null=True)
	conciencia = models.CharField(max_length=100, blank=True, default='', null=True)
	temperatura = models.FloatField(blank=True, null=True)

	descricao_clinica = models.TextField(blank=True, default='', null=True)

	image_descricao_clinica = models.BinaryField(blank=True, null=True, editable=True)

	sindrome_gripal = ArrayField(models.CharField(max_length=100), blank=True, null=True)
	tempo_quadro_sintomatico = models.IntegerField(blank=True, null=True)
	exposicao_pessoa_infectada = models.CharField(max_length=100, default='', blank=True, null=True)
	parentesco = models.CharField(max_length=100, blank=True, default='', null=True)
	comorbidades = ArrayField(models.CharField(max_length=100), blank=True, null=True)
	outras_comorbidades = models.CharField(max_length=100, blank=True, default='', null=True)
	outras_cardiopatias = models.CharField(max_length=100, blank=True, default='', null=True)
	idade_gestacional = models.CharField(max_length=100, blank=True, default='', null=True)
	comorbidades_obstetricas = models.CharField(max_length=100, blank=True, default='', null=True)
	gesta_para = models.CharField(max_length=100, blank=True, default='', null=True)

	medicamentos_uso_habitual = ArrayField(models.CharField(max_length=100), blank=True, null=True)
	medicamento_outros = models.CharField(max_length=100, blank=True, default='', null=True)

	spo2 = models.IntegerField(blank=True, null=True)
	fr_irpm = models.IntegerField(blank=True, null=True)

	ventilacao_tipo = models.CharField(max_length=100, blank=True, default='', null=True)
	
	o2_suporte = ArrayField(models.CharField(max_length=100), blank=True, null=True)
	dose_cn = models.FloatField(blank=True, null=True)
	dose_venturi = models.FloatField(blank=True, null=True)

	vmi = ArrayField(models.CharField(max_length=100), blank=True, null=True)

	vt = models.FloatField(blank=True, null=True)
	delta_pressure = models.FloatField(blank=True, null=True)
	pplato = models.FloatField(blank=True, null=True)
	raw = models.FloatField(blank=True, null=True)
	cest = models.FloatField(blank=True, null=True)
	sao2 = models.FloatField(blank=True, null=True)
	pao2 = models.FloatField(blank=True, null=True)
	fio2 = models.FloatField(blank=True, null=True)
	paco2 = models.FloatField(blank=True, null=True)

	pa = models.CharField(max_length=100, blank=True, default='', null=True)
	fc = models.IntegerField(blank=True, null=True)
	temperatura_axilar = models.FloatField(blank=True, null=True)

	droga_vasoativa = ArrayField(models.CharField(max_length=100), blank=True, null=True)
	qtd_nora = models.FloatField(blank=True, null=True)
	qtd_adrenalina = models.FloatField(blank=True, null=True)
	qtd_vasopressina = models.FloatField(blank=True, null=True)
	qtd_dobutamina = models.FloatField(blank=True, null=True)

	arritmia = ArrayField(models.CharField(max_length=100), blank=True, null=True)

	infeccao_bacteriana = models.CharField(max_length=100, blank=True, default='', null=True)
	foco = ArrayField(models.CharField(max_length=100), blank=True, null=True)

	uso_antibioticoterapia = models.CharField(max_length=200, blank=True, default='', null=True)

	pesquisa_teste_sars_cov_2 = models.CharField(max_length=100, blank=True, default='', null=True)

	igg = models.CharField(max_length=100, blank=True, default='', null=True)
	igm = models.CharField(max_length=100, blank=True, default='', null=True)
	data_igm_igg = models.DateField(blank=True, null=True, default=None)

	rt_pcr_sars_cov_2 = models.CharField(max_length=100, blank=True, default='', null=True)
	data_coleta = models.DateField(blank=True, null=True, default=None)

	em_uso_corticosteroide = models.CharField(max_length=100, blank=True, default='', null=True)
	dose_corticosteroide = models.CharField(max_length=100, blank=True, default='', null=True)
	data_inicio_corticosteroide = models.DateField(blank=True, null=True, default=None)

	em_uso_hidroxicloroquina = models.CharField(max_length=100, blank=True, default='', null=True)
	data_inicio_hidroxicloroquina = models.DateField(blank=True, null=True, default=None)

	em_uso_oseltamivir = models.CharField(max_length=100, blank=True, default='', null=True)
	data_inicio_oseltamivir = models.DateField(blank=True, null=True, default=None)

	em_uso_heparina = models.CharField(max_length=100, blank=True, default='', null=True)
	data_inicio_heparina = models.DateField(blank=True, null=True, default=None)
	tipo_heparina = models.CharField(max_length=100, blank=True, default='', null=True)
	dose_heparina = models.CharField(max_length=100, blank=True, default='', null=True)

	pps = models.FloatField(blank=True, null=True)

	escala_pontos_glasgow = models.IntegerField(blank=True, null=True)
	
	bloqueador_neuromuscular = ArrayField(models.CharField(max_length=100), blank=True, null=True)
	midazolam_dose = models.CharField(max_length=100, blank=True, default='', null=True)
	fentanil_dose = models.CharField(max_length=100, blank=True, default='', null=True)
	propofol_dose = models.CharField(max_length=100, blank=True, default='', null=True)

	sedacao_continua = ArrayField(models.CharField(max_length=100), blank=True, null=True)
	rocuronio_dose = models.CharField(max_length=100, blank=True, default='', null=True)
	pacuronio_dose = models.CharField(max_length=100, blank=True, default='', null=True)
	cisatracurio_dose = models.CharField(max_length=100, blank=True, default='', null=True)

	rass = models.CharField(max_length=100, blank=True, default='', null=True)

	data_exames_laboratorio = models.DateField(blank=True, null=True, default=None)
	leucocito = models.CharField(max_length=100, blank=True, default='', null=True)
	linfocito = models.CharField(max_length=100, blank=True, default='', null=True)
	hb = models.CharField(max_length=100, blank=True, default='', null=True)
	ht = models.CharField(max_length=100, blank=True, default='', null=True)
	pcr = models.CharField(max_length=100, blank=True, default='', null=True)
	lactato = models.CharField(max_length=100, blank=True, default='', null=True)
	dhl = models.CharField(max_length=100, blank=True, default='', null=True)
	ferritina = models.CharField(max_length=100, blank=True, default='', null=True)
	troponina = models.CharField(max_length=100, blank=True, default='', null=True)
	cpk = models.CharField(max_length=100, blank=True, default='', null=True)
	d_dimero = models.CharField(max_length=100, blank=True, default='', null=True)
	ureia = models.CharField(max_length=100, blank=True, default='', null=True)
	creatinina = models.CharField(max_length=100, blank=True, default='', null=True)
	ap = models.CharField(max_length=100, blank=True, default='', null=True)
	tap = models.CharField(max_length=100, blank=True, default='', null=True)
	inr = models.CharField(max_length=100, blank=True, default='', null=True)
	tgo = models.CharField(max_length=100, blank=True, default='', null=True)
	tgp = models.CharField(max_length=100, blank=True, default='', null=True)

	exame_imagem = ArrayField(models.CharField(max_length=100), blank=True, null=True)
	#laudo_tc_torax = models.TextField(blank=True, default='', null=True)
	#laudo_rx_torax = models.TextField(blank=True, default='', null=True)
	image_laudo_tc = models.BinaryField(blank=True, null=True, editable=True)
	image_laudo_rx = models.BinaryField(blank=True, null=True, editable=True)

	is_sindrome_gripal = models.CharField(max_length=100, blank=True, default='', null=True)
	news_fast_pb = models.CharField(max_length=100, blank=True, default='', null=True)
	news_modificado = models.CharField(max_length=100, blank=True, default='', null=True)
	uti = models.CharField(max_length=200, blank=True, default='', null=True)
	leito = models.CharField(max_length=100, blank=True, default='', null=True)

	parecer_medico = models.TextField(blank=True, default='', null=True)

	prioridade = models.IntegerField(blank=True, null=True)

	senha = models.IntegerField(blank=True, null=True)

	codigo_sescovid = models.CharField(max_length=100, blank=True, default='', null=True)

	justificativa = models.TextField(blank=True, default='', null=True)

	observacao = models.TextField(blank=True, default='', null=True)

	pareceristas  = ArrayField(models.CharField(max_length=100), blank=True, null=True)
	data_regulacao = models.DateTimeField(blank=True, null=True)

	andamento_processo = models.CharField(max_length=100, blank=True, default='', null=True)
	justificativa_cancelamento = models.TextField(blank=True, default='', null=True)
	data_cancelamento = models.DateTimeField(blank=True, null=True)

	last_status = models.CharField(max_length=200, blank=True, default='', null=True)

	data_obito = models.DateField(blank=True, null=True, default=None)




	def __str__(self):
		return str(self.nome_paciente)

class Cnes(models.Model):
	MUNICIPIO = models.CharField(max_length=200, blank=True, default='', null=True)
	NO_FANTASIA = models.CharField(max_length=200, blank=True, default='', null=True)
	CO_CNES = models.IntegerField(blank=True, null=True)

	def __str__(self):
		return str(self.MUNICIPIO)


class Status(models.Model):
	descricao = models.CharField(max_length=200, blank=True, default='', null=True)
	data_notificacao = models.DateField(auto_now_add=True)
	hora_notificacao = models.TimeField(auto_now_add=True)
	registro_covid = models.ForeignKey(RegistroCovid, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return str(self.descricao)

class Regulacao(models.Model):
	estabelecimento_referencia_covid = models.CharField(max_length=200, blank=True, default='', null=True)
	nome_paciente = models.CharField(max_length=200, blank=True, default='', null=True)
	data_notificacao = models.DateField(auto_now_add=True)
	hora_notificacao = models.TimeField(auto_now_add=True)
	senha = models.IntegerField(blank=True, null=True)
	registro_covid = models.ForeignKey(RegistroCovid, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return str(self.estabelecimento_referencia_covid)