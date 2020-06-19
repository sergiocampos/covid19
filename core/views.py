from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime, timezone
from .models import RegistroCovid
import calendar
from time import gmtime, strftime
from django.core.paginator import Paginator

# Create your views here.

@login_required
def covid_list(request):
	registros = RegistroCovid.objects.all()

	paginator = Paginator(registros, 10)
	page = request.GET.get('page')
	regs = paginator.get_page(page)

	return render(request, 'list.html', {'regs':regs})


@login_required
def registro_covid(request):
	data = datetime.now()
	formateDate = data.strftime("%d-%m-%Y")
	hora = data.strftime("%H:%M")

	last_registro = RegistroCovid.objects.all().last()
	if not last_registro:
		last_codigo_registro_total = 0
		last_codigo_registro_mensal = 0
	else:
		last_codigo_registro_total = last_registro.codigo_registro_total
		last_codigo_registro_mensal = last_registro.codigo_registro_mensal
	

	#Dia de hoje:
	dia = data.day
	#mês:
	mes_ultimo_registro=last_registro.data_notificacao.month
	mes_corrente=data.month
	dia_h=last_registro.data_notificacao.day
	print("Mês do último registro:", mes_ultimo_registro, type(mes_ultimo_registro))
	print("Mês corrente:", mes_corrente, type(mes_corrente))
	print("dia do último registro:", dia_h)
	#Verifica se o mês mudou:
	if mes_corrente > mes_ultimo_registro:
		last_codigo_registro_mensal = 1
		last_codigo_registro_total += 1
	else:
		last_codigo_registro_total += 1
		last_codigo_registro_mensal += 1


	print("codigo total de registro:", last_codigo_registro_total)
	print("codigo mensal de registro:", last_codigo_registro_mensal)
	#último dia do mês:
	#ultimo_dia = calendar.monthrange(int(strftime("%Y", gmtime())), int(strftime("%m", gmtime())))[1]
	#if dia <= ultimo_dia:
	#	last_codigo_registro_total += 1
	#	last_codigo_registro_mensal += 1
	#else:
	#	last_codigo_registro_total += 1
	#	last_codigo_registro_mensal += 0

	last_codigo_registro_total_str = str(last_codigo_registro_total)
	last_codigo_registro_mensal_str = str(last_codigo_registro_mensal)


	num_registro = last_codigo_registro_total_str + last_codigo_registro_mensal_str

	return render(request, 'registro_covid.html', {'formateDate': formateDate, 'hora': hora, 'num_registro':num_registro, 'last_codigo_registro_total_str': last_codigo_registro_total_str, 'last_codigo_registro_mensal_str':last_codigo_registro_mensal_str})


@login_required
def registro_covid_set(request):
	
	responsavel_pelo_preenchimento = request.user

	data = datetime.now()
	data_notificacao = data.strftime("%d-%m-%Y")
	hora_notificacao = data.strftime("%H:%M")

	#data_notificacao = request.POST.get('data_notificacao')
	#hora_notificacao = request.POST.get('hora_notificacao')
	
	nome_solicitante = request.POST.get('nome_solicitante')
	municipio_estabelecimento = request.POST.get("municipio_do_estabelecimento")
	estabelecimento_solicitante = request.POST.get('estabelecimento_solicitante')
	estabelecimento_outro = request.POST.get('desc_outro_estabelecimento')
	unidade_origem = request.POST.get('unidade_origem')
	nome_paciente = request.POST.get('nome_paciente')
	
	idade_paciente_cap = request.POST.get('idade_paciente')
	if idade_paciente_cap != '':
		idade_paciente = int(idade_paciente_cap)
	else:
		idade_paciente = None
	
	recurso_que_precisa = request.POST.get('recurso_que_precisa')
	estado_origem = request.POST.get('estado_paciente')
	cidade_origem = request.POST.get('cidade_paciente')
	telefone_retorno = request.POST.get('telefone_retorno')

	frequencia_respiratoria_cap = request.POST.get('frequencia_respiratoria')
	if frequencia_respiratoria_cap != '':
		frequencia_respiratoria = int(frequencia_respiratoria_cap)
	else:
		frequencia_respiratoria = None

	saturacao_paciente_cap = request.POST.get('saturacao_paciente')
	if saturacao_paciente_cap != '':
		saturacao_paciente = int(saturacao_paciente_cap)
	else:
		saturacao_paciente = None

	ar_o2 = request.POST.get('ar_o2')
	
	frequencia_cardiaca_cap = request.POST.get('f_cardiaca_paciente')
	if frequencia_cardiaca_cap != '':
		frequencia_cardiaca = int(frequencia_cardiaca_cap)
	else:
		frequencia_cardiaca = None

	pa_part1 = request.POST.get('pa_part1')
	pa_part2 = request.POST.get('pa_part2')

	pa = pa_part1 +"x"+ pa_part2
	conciencia = request.POST.get('consciencia_paciente')
	
	temperatura_cap = request.POST.get('temperatura_paciente')
	if temperatura_cap != '':
		temperatura = float(temperatura_cap)
	else:
		temperatura = None

	observacao = request.POST.get('observacao_paciente')


	#implementar o algoritmo: codigo_registro = None
	codigo_registro_total = request.POST.get('last_codigo_total')
	codigo_registro_mensal = request.POST.get('last_codigo_mensal')


	codigo_registro_completo = request.POST.get('num_total_registros')

	registro = RegistroCovid.objects.create(
		responsavel_pelo_preenchimento = responsavel_pelo_preenchimento,
		codigo_registro_total = codigo_registro_total,
		codigo_registro_mensal = codigo_registro_mensal,
		codigo_registro_completo = codigo_registro_completo,
		nome_solicitante = nome_solicitante,
		municipio_estabelecimento = municipio_estabelecimento,
		estabelecimento_solicitante = estabelecimento_solicitante,
		estabelecimento_outro = estabelecimento_outro,
		unidade_origem = unidade_origem,
		nome_paciente = nome_paciente,
		idade_paciente = idade_paciente,
		recurso_que_precisa = recurso_que_precisa,
		estado_origem = estado_origem,
		cidade_origem = cidade_origem,
		telefone_retorno = telefone_retorno,
		frequencia_respiratoria = frequencia_respiratoria,
		saturacao_paciente = saturacao_paciente,
		ar_o2 = ar_o2,
		frequencia_cardiaca = frequencia_cardiaca,
		pa = pa,
		conciencia = conciencia,
		temperatura = temperatura,
		observacao = observacao

		)



	return redirect('covid_list')

@login_required
def registro_enfermeiro_medico(request):
    return render(request, 'registro_enfermeiro_medico.html')

@login_required
def regulacao(request, id):

	registro = RegistroCovid.objects.get(id=id)
	pa = registro.pa

	p = pa.split("x")
	pa_1 = p[0]
	pa_2 = p[1]

	return render(request, 'regulacao.html', {'registro' : registro, 'pa_1':pa_1, 'pa_2':pa_2})


@login_required
def regulacao_set(request, id):
	registro = RegistroCovid.objects.get(id=id)

	responsavel_pelo_preenchimento = request.user
	
	
	nome_solicitante = request.POST.get('nome_solicitante')
	municipio_estabelecimento = registro.municipio_estabelecimento
	estabelecimento_solicitante = registro.estabelecimento_solicitante
	estabelecimento_outro = registro.estabelecimento_outro
	unidade_origem = request.POST.get('unidade_origem')
	nome_paciente = request.POST.get('nome_paciente')
	
	idade_paciente_cap = request.POST.get('idade_paciente')
	if idade_paciente_cap == '' or idade_paciente_cap == None:
		idade_paciente = None
	else:
		idade_paciente = int(float(idade_paciente_cap))

	recurso_que_precisa = registro.recurso_que_precisa
	estado_origem = registro.estado_origem
	cidade_origem = registro.cidade_origem
	telefone_retorno = registro.telefone_retorno
	frequencia_respiratoria = registro.frequencia_respiratoria
	saturacao_paciente = registro.saturacao_paciente
	ar_o2 = registro.ar_o2
	frequencia_cardiaca = registro.frequencia_cardiaca
	
	pa_part1 = request.POST.get('pa_part1')
	pa_part2 = request.POST.get('pa_part2')
	pa = pa_part1 + "x" + pa_part2
	
	conciencia = registro.conciencia
	temperatura = registro.temperatura

	descricao_clinica = request.POST.get('descricao_clinica')
	
	sindrome_gripal = request.POST.getlist('s_gripal')
	
	tempo_quadro_sintomatico_cap = request.POST.get('tempo_inicio_sintomas')
	if tempo_quadro_sintomatico_cap == '' or tempo_quadro_sintomatico_cap == None:
		tempo_quadro_sintomatico = None
	else:
		tempo_quadro_sintomatico = int(float(tempo_quadro_sintomatico_cap))

	exposicao_pessoa_infectada = request.POST.get('exposicao_epidemiologica_sim')
	parentesco = request.POST.get('grau_parentesco')
	comorbidades = request.POST.getlist('comorbidades')
	outras_comorbidades = request.POST.get('descricao_outras_comorbidades')
	outras_cardiopatias = request.POST.get('desc_outras_cardiopatias')
	idade_gestacional = request.POST.get('idade_gestacao')
	comorbidades_obstetricas = request.POST.get('comorbidade_obstetrica')
	gesta_para = request.POST.get('gestacao_para')
	medicamentos_uso_habitual = request.POST.getlist('medicamento_uso_habitual')
	medicamento_outros = request.POST.get('descricao_outros_medicamento')
	
	spo2_cap = request.POST.get('spo2')
	if spo2_cap == '' or spo2_cap == None:
		spo2 = None
	else:
		spo2 = int(float(spo2_cap))
		

	fr_irpm_cap = request.POST.get('fr_irpm')
	if fr_irpm_cap == '' or fr_irpm_cap == None:
		fr_irpm = None
	else:
		fr_irpm = int(float(fr_irpm_cap))
		

	ventilacao_tipo = request.POST.get('ventilacao')
	o2_suporte = request.POST.getlist('o2_suporte')
	
	dose_cn_cap = request.POST.get('dose_cn')
	if dose_cn_cap == '' or dose_cn_cap == None:
		dose_cn = None
	else:
		dose_cn = float(dose_cn_cap)

	dose_venturi_cap = request.POST.get('dose_venturi')
	if dose_venturi_cap == '' or dose_venturi_cap == None:
		dose_venturi = None
	else:
		dose_venturi = float(dose_venturi_cap)
	

	vmi = request.POST.getlist('vmi')
	
	vt_cap = request.POST.get('vt')
	if vt_cap == '' or vt_cap == None:
		vt = None
	else:
		vt = float(vt_cap)
		

	delta_pressure_cap = request.POST.get('delta_pressure')
	if delta_pressure_cap == '' or delta_pressure_cap == None:
		delta_pressure = None
	else:
		delta_pressure = float(delta_pressure_cap)
		

	pplato_cap = request.POST.get('pplato')
	if pplato_cap == '' or pplato_cap == None:
		pplato = None
	else:
		pplato = float(pplato_cap)
		

	raw_cap = request.POST.get('raw')
	if raw_cap == '' or raw_cap == None:
		raw = None
	else:
		raw = float(raw_cap)
		

	cest_cap = request.POST.get('cest')
	if cest_cap == '' or cest_cap == None :
		cest = None
	else:
		cest = float(cest_cap)
		

	sao2_cap = request.POST.get('sao2')
	if sao2_cap == '' or sao2_cap == None:
		sao2 = None
	else:
		sao2 = float(sao2_cap)

	pao2_cap = request.POST.get('pao2')
	if pao2_cap == '' or pao2_cap == None:
		pao2 = None
	else:
		pao2 = float(pao2_cap)

	fio2_cap = request.POST.get('fio2')
	if fio2_cap == '' or fio2_cap == None:
		fio2 = None
	else:
		fio2 = float(fio2_cap)

	paco2_cap = request.POST.get('paco2')
	if paco2_cap == '' or paco2_cap == None:
		paco2 = None
	else:
		paco2 = float(paco2_cap)
	
	fc_cap = request.POST.get('fc')
	if fc_cap == '' or fc_cap == None:
		fc = None
	else:
		fc = int(float(fc_cap))
		

	temperatura_axilar_cap = request.POST.get('temp_auxiliar')
	if temperatura_axilar_cap == '' or temperatura_axilar_cap == None :
		temperatura_axilar = None
	else:
		temperatura_axilar = float(temperatura_axilar_cap)
		

	droga_vasoativa = request.POST.getlist('droga_vasoativa')
	
	qtd_nora_cap = request.POST.get('qtd_nora')
	if qtd_nora_cap == '' or qtd_nora_cap == None:
		qtd_nora = None
	else:
		qtd_nora = float(qtd_nora_cap)

	qtd_adrenalina_cap = request.POST.get('qtd_adrenalina')
	if qtd_adrenalina_cap == '' or qtd_adrenalina_cap == None:
		qtd_adrenalina = None
	else:
		qtd_adrenalina = float(qtd_adrenalina_cap)

	qtd_vasopressina_cap = request.POST.get('qtd_vasopressina')
	if qtd_vasopressina_cap == '' or qtd_vasopressina_cap == None:
		qtd_vasopressina = None
	else:
		qtd_vasopressina = float(qtd_vasopressina_cap)

	qtd_dobutamina_cap = request.POST.get('qtd_dobutamina')
	if qtd_dobutamina_cap == '' or qtd_dobutamina_cap == None:
		qtd_dobutamina = None
	else:
		qtd_dobutamina = float(qtd_dobutamina_cap)

	arritmia = request.POST.getlist('arritmia')
	infeccao_bacteriana = request.POST.get('infeccao_bacteriana')
	foco = request.POST.getlist('foco')
	uso_antibioticoterapia = request.POST.get('uso_antibioticoterapia')
	pesquisa_teste_sars_cov_2 = request.POST.get('pesquisa_sars_cov2')
	rt_pcr_sars_cov_2 = request.POST.get('pcr_sars_cov2')
	
	data_da_coleta_bd_cap = request.POST.get('data_da_coleta_bd')
	data_coleta_cap = request.POST.get('data_da_coleta')
	if data_coleta_cap == '' or data_coleta_cap == None:
		if data_da_coleta_bd_cap == '' or data_da_coleta_bd_cap == None:
			data_coleta = None
		else:
			data_coleta = datetime.strptime(data_da_coleta_bd_cap, '%d/%m/%Y').date()
	else:
		data_coleta = data_coleta_cap
	
	em_uso_corticosteroide = request.POST.get('em_uso_corticosteroide')
	dose_corticosteroide = request.POST.get('dose_corticosteroide')
	
	data_inicio_corticosteroide_bd_cap = request.POST.get('data_inicio_corticosteroide_bd')
	data_inicio_corticosteroide_cap = request.POST.get('data_inicio_corticosteroide')
	if data_inicio_corticosteroide_cap == '' or data_inicio_corticosteroide_cap == None:
		if data_inicio_corticosteroide_bd_cap == '' or data_inicio_corticosteroide_bd_cap == None:
			data_inicio_corticosteroide = None
		else:
			data_inicio_corticosteroide = datetime.strptime(data_inicio_corticosteroide_bd_cap, '%d/%m/%Y').date()
	else:
		data_inicio_corticosteroide = data_inicio_corticosteroide_cap
	

	em_uso_hidroxicloroquina = request.POST.get('em_uso_hidrocloroquina')
	
	data_inicio_hidroxicloroquina_cap = request.POST.get('data_inicio_hidroxicloroquina')
	data_inicio_hidroxicloroquina_bd_cap = request.POST.get('data_inicio_hidroxicloroquina_bd')


	if data_inicio_hidroxicloroquina_cap == '' or data_inicio_hidroxicloroquina_cap == None:
		if data_inicio_hidroxicloroquina_bd_cap == '' or data_inicio_hidroxicloroquina_bd_cap == None:
			data_inicio_hidroxicloroquina = None	
		else:
			data_inicio_hidroxicloroquina = datetime.strptime(data_inicio_hidroxicloroquina_bd_cap, '%d/%m/%Y').date()
	else:
		data_inicio_hidroxicloroquina = data_inicio_hidroxicloroquina_cap


	

	em_uso_oseltamivir = request.POST.get('em_uso_oseltamivir')
	
	data_inicio_oseltamivir_cap = request.POST.get('data_inicio_oseltamivir')
	data_inicio_oseltamivir_bd_cap = request.POST.get('data_inicio_oseltamivir_bd')


	if data_inicio_oseltamivir_cap == '' or data_inicio_oseltamivir_cap == None:
		if data_inicio_oseltamivir_bd_cap == '' or data_inicio_oseltamivir_bd_cap == None:
			data_inicio_oseltamivir = None
		else:
			data_inicio_oseltamivir = datetime.strptime(data_inicio_oseltamivir_bd_cap, '%d/%m/%Y').date()
	else:
		data_inicio_oseltamivir = data_inicio_oseltamivir_cap



	em_uso_heparina = request.POST.get('em_uso_heparina')

	data_inicio_heparina_bd_cap = request.POST.get('data_inicio_heparina_bd')
	data_inicio_heparina_cap = request.POST.get('data_inicio_heparina')

	if data_inicio_heparina_cap == '' or data_inicio_heparina_cap == None:
		if data_inicio_heparina_bd_cap == '' or data_inicio_heparina_bd_cap == None:
			data_inicio_heparina = None
		else:
			data_inicio_heparina = datetime.strptime(data_inicio_heparina_bd_cap, '%d/%m/%Y').date()
	else:
		data_inicio_heparina = data_inicio_heparina_cap
		

	tipo_heparina = request.POST.get('tipo_heparina')
	dose_heparina = request.POST.get('dose_heparina')
	
	pps_cap = request.POST.get('pps_paciente')
	if pps_cap == '' or pps_cap == None:
		pps = None
	else:
		pps = float(pps_cap)
		

	escala_pontos_glasgow_cap = request.POST.get('escala_glasgow')
	if escala_pontos_glasgow_cap == '' or escala_pontos_glasgow_cap == None:
		escala_pontos_glasgow = None
	else:
		escala_pontos_glasgow = int(float(escala_pontos_glasgow_cap))
		

	bloqueador_neuromuscular = request.POST.getlist('desc_bloqueador_neuromuscular')
	midazolam_dose = request.POST.get('midazolam_dose')
	fentanil_dose = request.POST.get('fentanil_dose')
	propofol_dose = request.POST.get('propofol_dose')
	sedacao_continua = request.POST.getlist('desc_sedacao_continua')
	rocuronio_dose = request.POST.get('rocuronio_dose')
	pacuronio_dose = request.POST.get('pacuronio_dose')
	cisatracurio_dose = request.POST.get('cisatracurio_dose')
	rass = request.POST.get('rass')
	
	data_exames_laboratorio_cap = request.POST.get('data_exames_laboratorio')
	data_exames_laboratorio_bd_cap = request.POST.get('data_exames_laboratorio_bd')

	if data_exames_laboratorio_cap == '' or data_exames_laboratorio_cap == None:
		if data_exames_laboratorio_bd_cap == '' or data_exames_laboratorio_bd_cap == None:
			data_exames_laboratorio = None
		else:
			data_exames_laboratorio = datetime.strptime(data_exames_laboratorio_bd_cap, '%d/%m/%Y').date()
	else:
		data_exames_laboratorio = data_exames_laboratorio_cap

	leucocito = request.POST.get('leucocito')
	linfocito = request.POST.get('linfocito')
	hb = request.POST.get('hb')
	ht = request.POST.get('ht')
	pcr = request.POST.get('pcr')
	lactato = request.POST.get('lactato')
	dhl = request.POST.get('dhl')
	ferritina = request.POST.get('ferritina')
	troponina = request.POST.get('troponina')
	cpk = request.POST.get('cpk')
	d_dimero = request.POST.get('d_dimero')
	ureia = request.POST.get('ureia')
	creatinina = request.POST.get('creatinina')
	ap = request.POST.get('ap')
	tap = request.POST.get('tap')
	inr = request.POST.get('inr')
	tgo = request.POST.get('tgo')
	tgp = request.POST.get('tgp')
	exame_imagem = request.POST.getlist('exame_imagem')
	laudo_tc_torax = request.POST.get('laudo_tc_torax')
	laudo_rx_torax = request.POST.get('laudo_rx_torax')
	is_sindrome_gripal = request.POST.get('sindrome_gripal')
	news_fast_pb = request.POST.get('new_fast')
	news_modificado = request.POST.get('new_modificado')
	uti = request.POST.get('uti')
	leito = request.POST.get('perfil')

	parecer_medico = request.POST.get('parecer')
	
	prioridade_cap = request.POST.get('prioridade')
	if prioridade_cap == '' or prioridade_cap == None:
		prioridade = None
	else:
		prioridade = int(float(prioridade_cap))
		

	status_regulacao = registro.status_regulacao
	
	regulacao_paciente = request.POST.get('paciente_preenche_criterios')

	status_regulacao_cap = request.POST.getlist('status_paciente')

	if regulacao_paciente == 'Paciente não preenche critérios para Regulação':
		if status_regulacao == '' or status_regulacao == None:
			status_regulacao = '{Paciente Não Regulado}'
		else:
			#n = 'Paciente Não Regulado'
			status_regulacao.append(status_regulacao_cap)
		#else:
		#	status_regulacao = status_regulacao + status_regulacao_cap
	elif regulacao_paciente == 'Paciente preenche critérios para Regulação':
		if status_regulacao == '' or status_regulacao == None:
			status_regulacao = '{Paciente Regulado, Aguardando confirmação de Vaga}'
		else:
			status_regulacao.append(status_regulacao_cap)
	else:
		status_regulacao = '{}'
	
	print("Status da regulação:", status_regulacao)	

	#status_regulacao = request.POST.get('')
	codigo_sescovid = request.POST.get('num_protocolo')
	justificativa = request.POST.get('justificativa')
	observacao = request.POST.get('observacoes_medicas')
	
	pareceristas = registro.pareceristas
	
	pareceristas_cap = request.POST.getlist('pareceristas')
	
	if pareceristas == '' or pareceristas == None:
		pareceristas = pareceristas_cap
	else:
		pareceristas = pareceristas + pareceristas_cap

	data_regulacao_bd_cap = request.POST.get('data_regulacao_bd')
	data_regulacao_cap = request.POST.get('data_regulacao')
	if data_regulacao_cap == '' or data_regulacao_cap == None:
		if data_regulacao_bd_cap == '' or data_regulacao_bd_cap == None:
			data_regulacao = None
		else:
			data_regulacao = datetime.strptime(data_regulacao_bd_cap, '%d/%m/%Y').date()
	else:
		data_regulacao = data_regulacao_cap


	data_obito_bd_cap = request.POST.get('data_obito_bd')
	data_obito_cap = request.POST.get('data_obito')

	if data_obito_cap == '' or data_obito_cap == None:
		if data_obito_bd_cap == '' or data_obito_bd_cap == None:
			data_obito = None
		else:
			data_obito = datetime.strptime(data_obito_bd_cap, '%d/%m/%Y').date()
	else:
		data_obito = data_obito_cap

	
	registro.responsavel_pelo_preenchimento = responsavel_pelo_preenchimento
	#registro.codigo_registro = codigo_registro
	registro.nome_solicitante = nome_solicitante
	registro.municipio_estabelecimento = municipio_estabelecimento
	registro.estabelecimento_solicitante = estabelecimento_solicitante
	registro.estabelecimento_outro = estabelecimento_outro
	registro.unidade_origem = unidade_origem
	registro.nome_paciente = nome_paciente
	registro.idade_paciente = idade_paciente
	registro.recurso_que_precisa = recurso_que_precisa
	registro.estado_origem = estado_origem
	registro.cidade_origem = cidade_origem
	registro.telefone_retorno = telefone_retorno
	registro.frequencia_respiratoria = frequencia_respiratoria
	registro.saturacao_paciente = saturacao_paciente
	registro.ar_o2 = ar_o2
	registro.frequencia_cardiaca = frequencia_cardiaca
	registro.pa = pa
	registro.conciencia = conciencia
	registro.temperatura = temperatura
	registro.descricao_clinica = descricao_clinica
	registro.sindrome_gripal = sindrome_gripal
	registro.tempo_quadro_sintomatico = tempo_quadro_sintomatico
	registro.exposicao_pessoa_infectada = exposicao_pessoa_infectada
	registro.parentesco = parentesco
	registro.comorbidades = comorbidades
	registro.outras_comorbidades = outras_comorbidades
	registro.outras_cardiopatias = outras_cardiopatias
	registro.idade_gestacional = idade_gestacional
	registro.comorbidades_obstetricas = comorbidades_obstetricas
	registro.gesta_para = gesta_para
	registro.medicamentos_uso_habitual = medicamentos_uso_habitual
	registro.medicamento_outros = medicamento_outros
	registro.spo2 = spo2
	registro.fr_irpm = fr_irpm
	registro.ventilacao_tipo = ventilacao_tipo
	registro.o2_suporte = o2_suporte
	registro.dose_cn = dose_cn
	registro.dose_venturi = dose_venturi
	registro.vmi = vmi
	registro.vt = vt
	registro.delta_pressure = delta_pressure
	registro.pplato = pplato
	registro.raw = raw
	registro.cest = cest
	registro.sao2 = sao2
	registro.pao2 = pao2
	registro.fio2 = fio2
	registro.paco2 = paco2
	registro.pa = pa
	registro.fc = fc
	registro.temperatura_axilar = temperatura_axilar
	registro.droga_vasoativa = droga_vasoativa
	registro.qtd_nora = qtd_nora
	registro.qtd_adrenalina = qtd_adrenalina
	registro.qtd_vasopressina = qtd_vasopressina
	registro.qtd_dobutamina = qtd_dobutamina
	registro.arritmia = arritmia
	registro.infeccao_bacteriana = infeccao_bacteriana
	registro.foco = foco
	registro.uso_antibioticoterapia = uso_antibioticoterapia
	registro.pesquisa_teste_sars_cov_2 = pesquisa_teste_sars_cov_2
	registro.rt_pcr_sars_cov_2 = rt_pcr_sars_cov_2
	registro.data_coleta = data_coleta
	registro.em_uso_corticosteroide = em_uso_corticosteroide
	registro.dose_corticosteroide = dose_corticosteroide
	registro.data_inicio_corticosteroide = data_inicio_corticosteroide
	registro.em_uso_hidroxicloroquina = em_uso_hidroxicloroquina
	registro.data_inicio_hidroxicloroquina = data_inicio_hidroxicloroquina
	registro.em_uso_oseltamivir = em_uso_oseltamivir
	registro.data_inicio_oseltamivir = data_inicio_oseltamivir
	registro.em_uso_heparina = em_uso_heparina
	registro.data_inicio_heparina = data_inicio_heparina
	registro.tipo_heparina = tipo_heparina
	registro.dose_heparina = dose_heparina
	registro.pps = pps
	registro.escala_pontos_glasgow = escala_pontos_glasgow
	registro.bloqueador_neuromuscular = bloqueador_neuromuscular
	registro.midazolam_dose = midazolam_dose
	registro.fentanil_dose = fentanil_dose
	registro.propofol_dose = propofol_dose
	registro.sedacao_continua = sedacao_continua
	registro.rocuronio_dose = rocuronio_dose
	registro.pacuronio_dose = pacuronio_dose
	registro.cisatracurio_dose = cisatracurio_dose
	registro.rass = rass
	registro.data_exames_laboratorio = data_exames_laboratorio
	registro.leucocito = leucocito
	registro.linfocito = linfocito
	registro.hb = hb
	registro.ht = ht
	registro.pcr = pcr
	registro.lactato = lactato
	registro.dhl = dhl
	registro.ferritina = ferritina
	registro.troponina = troponina
	registro.cpk = cpk
	registro.d_dimero = d_dimero
	registro.ureia = ureia
	registro.creatinina = creatinina
	registro.ap = ap
	registro.tap = tap
	registro.inr = inr
	registro.tgo = tgo
	registro.tgp = tgp
	registro.exame_imagem = exame_imagem
	registro.laudo_tc_torax = laudo_tc_torax
	registro.laudo_rx_torax = laudo_rx_torax
	registro.is_sindrome_gripal = is_sindrome_gripal
	registro.news_fast_pb = news_fast_pb
	registro.news_modificado = news_modificado
	registro.uti = uti
	registro.leito = leito
	registro.parecer_medico = parecer_medico
	registro.prioridade = prioridade
	registro.regulacao_paciente = regulacao_paciente
	registro.status_regulacao = status_regulacao
	registro.codigo_sescovid = codigo_sescovid
	registro.justificativa = justificativa
	registro.observacao = observacao
	registro.pareceristas = pareceristas
	registro.data_regulacao = data_regulacao
	registro.data_obito = data_obito

	registro.save()

	return redirect('regulacao_detail', id=id)


@login_required
def regulacao_detail(request, id):
	registro = RegistroCovid.objects.get(id=id)

	responsavel_pelo_preenchimento = request.user

	pa = registro.pa
	p = pa.split("x")
	p1 = p[0]
	p2 = p[1]

	

	return render(request, 'regulacao_detail.html', {'registro':registro, 'p1':p1, 'p2':p2})

@login_required
def regulacao_edit(request, id):

	#registro_id = request.GET.get('id')
	#registro = RegistroCovid.objects.get(id=registro_id)
	registro = RegistroCovid.objects.get(id=id)
	pa = registro.pa
	p = pa.split("x")
	p1 = p[0]
	p2 = p[1]

	return render(request, 'regulacao_edit.html', {'registro':registro, 'p1': p1, 'p2': p2})

@login_required
def regulacao_edit_set(request, id):

	registro = RegistroCovid.objects.get(id=id)

	
	responsavel_pelo_preenchimento = request.user

	#data = datetime.now()
	#data_notificacao = data.strftime("%d-%m-%Y")
	#hora_notificacao = data.strftime("%H:%M")

	#data_notificacao = request.POST.get('data_notificacao')
	#hora_notificacao = request.POST.get('hora_notificacao')
	
	nome_solicitante = request.POST.get('nome_solicitante')
	municipio_estabelecimento = request.POST.get("municipio_do_estabelecimento")
	estabelecimento_solicitante = request.POST.get('estabelecimento_solicitante')
	estabelecimento_outro = request.POST.get('desc_outro_estabelecimento')
	unidade_origem = request.POST.get('unidade_origem')
	nome_paciente = request.POST.get('nome_paciente')
	
	idade_paciente_cap = request.POST.get('idade_paciente')
	if idade_paciente_cap != '':
		idade_paciente = int(idade_paciente_cap)
	else:
		idade_paciente = None
	
	recurso_que_precisa = request.POST.get('recurso_que_precisa')
	#estado_origem = request.POST.get('estado_paciente')
	cidade_origem = request.POST.get('cidade_origem')
	telefone_retorno = request.POST.get('telefone_retorno')

	frequencia_respiratoria_cap = request.POST.get('frequencia_respiratoria')
	if frequencia_respiratoria_cap != '':
		frequencia_respiratoria = int(frequencia_respiratoria_cap)
	else:
		frequencia_respiratoria = None

	saturacao_paciente_cap = request.POST.get('saturacao_paciente')
	if saturacao_paciente_cap != '':
		saturacao_paciente = int(saturacao_paciente_cap)
	else:
		saturacao_paciente = None

	ar_o2 = request.POST.get('ar_o2')
	
	frequencia_cardiaca_cap = request.POST.get('f_cardiaca_paciente')
	if frequencia_cardiaca_cap != '':
		frequencia_cardiaca = int(frequencia_cardiaca_cap)
	else:
		frequencia_cardiaca = None

	pa_part1 = request.POST.get('pa_part1')
	pa_part2 = request.POST.get('pa_part2')

	pa = pa_part1 +"x"+ pa_part2
	conciencia = request.POST.get('consciencia_paciente')
	
	temperatura_cap = request.POST.get('temperatura_paciente')
	if temperatura_cap != '':
		temperatura = float(temperatura_cap)
	else:
		temperatura = None

	observacao = request.POST.get('observacao_paciente')

	
	registro.responsavel_pelo_preenchimento = responsavel_pelo_preenchimento
	registro.nome_solicitante = nome_solicitante
	registro.municipio_estabelecimento = municipio_estabelecimento
	registro.estabelecimento_solicitante = estabelecimento_solicitante
	registro.estabelecimento_outro = estabelecimento_outro
	registro.unidade_origem = unidade_origem
	registro.nome_paciente = nome_paciente
	registro.idade_paciente = idade_paciente
	registro.recurso_que_precisa = recurso_que_precisa
	#registro.estado_origem = estado_origem
	registro.cidade_origem = cidade_origem
	registro.telefone_retorno = telefone_retorno
	registro.frequencia_respiratoria = frequencia_respiratoria
	registro.saturacao_paciente = saturacao_paciente
	registro.ar_o2 = ar_o2
	registro.frequencia_cardiaca = frequencia_cardiaca
	registro.pa = pa
	registro.conciencia = conciencia
	registro.temperatura = temperatura	
	registro.observacao = observacao
	

	registro.save()

	return redirect('covid_list')

@login_required
def search_register(request):
	registros = RegistroCovid.objects.all()

	paginator = Paginator(registros, 5)
	page = request.GET.get('page')
	regs = paginator.get_page(page)

	return render(request, 'search_register.html', {'regs':regs})

@login_required
def search_between_date(request):

	return render(request, 'search_between_date.html')

@login_required
def search_between_date_set(request):
	data_inicio = request.POST.get('data_inicio')
	data_fim = request.POST.get('data_fim')

	values = RegistroCovid.objects.filter(data_notificacao__range=[data_inicio, data_fim])
		
	return render(request, 'result_search_between_date.html', {'values':values})

@login_required
def result_search_between_date(request):


	return render(request, 'result_search_between_date.html')