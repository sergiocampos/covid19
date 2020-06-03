from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime, timezone
from .models import RegistroCovid
import calendar
from time import gmtime, strftime

# Create your views here.

@login_required
def covid_list(request):
	registros = RegistroCovid.objects.all()
	return render(request, 'list.html', {'registros':registros})


@login_required
def registro_covid(request):
	data = datetime.now()
	formateDate = data.strftime("%d-%m-%Y")
	hora = data.strftime("%H:%M")

	last_registro = RegistroCovid.objects.all().last()
	last_codigo_registro_total = last_registro.codigo_registro_total
	last_codigo_registro_mensal = last_registro.codigo_registro_mensal
	

	#Dia de hoje:
	dia = data.day
	#último dia do mês:
	ultimo_dia = calendar.monthrange(int(strftime("%Y", gmtime())), int(strftime("%m", gmtime())))[1]
	if dia <= ultimo_dia:
		last_codigo_registro_total += 1
		last_codigo_registro_mensal += 1
	else:
		last_codigo_registro_total += 1
		last_codigo_registro_mensal += 0

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

	observacoes = request.POST.get('observacao_paciente')


	#implementar o algoritmo: codigo_registro = None
	codigo_registro_total = request.POST.get('last_codigo_total')
	codigo_registro_mensal = request.POST.get('last_codigo_mensal')


	codigo_registro_completo = request.POST.get('num_total_registros')
	print("codigo completo:",codigo_registro_completo)

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
		observacoes = observacoes

		)



	return redirect('covid_list')

@login_required
def registro_enfermeiro_medico(request):
    return render(request, 'registro_enfermeiro_medico.html')

@login_required
def regulacao(request, id):

	registro = RegistroCovid.objects.get(id=id)
	pa = registro.pa

	if len(pa)>4:
		pa_1 = pa[0] + pa[1]
		pa_2 = pa[3] + pa[4]
	elif len(pa) == 4:
		pa_1 = pa[0] + pa[1]
		pa_2 = pa[3]
	else:
		pa_1 = ''
		pa_2 = ''

	return render(request, 'regulacao.html', {'registro' : registro, 'pa_1':pa_1, 'pa_2':pa_2})


@login_required
def regulacao_set(request, id):
	registro = RegistroCovid.objects.get(id=id)

	responsavel_pelo_preenchimento = request.user
	
	codigo_registro = "20201"
	#implementar
	nome_solicitante = request.POST.get('nome_solicitante')
	municipio_estabelecimento = request.POST.get('')
	estabelecimento_solicitante = request.POST.get('')
	estabelecimento_outro = request.POST.get('')
	unidade_origem = request.POST.get('unidade_origem')
	nome_paciente = request.POST.get('nome_paciente')
	idade_paciente = request.POST.get('idade_paciente')
	recurso_que_precisa = request.POST.get('')
	estado_origem = request.POST.get('')
	cidade_origem = request.POST.get('')
	telefone_retorno = request.POST.get('')
	frequencia_respiratoria = request.POST.get('')
	saturacao_paciente = request.POST.get('')
	ar_o2 = request.POST.get('')
	frequencia_cardiaca = request.POST.get('')
	
	pa_part1 = request.POST.get('pa_part1')
	pa_part2 = request.POST.get('pa_part2')
	pa = pa_part1 + "x" + pa_part2
	
	conciencia = request.POST.get('')
	temperatura = request.POST.get('')
	observacoes = request.POST.get('')
	sindrome_gripal = request.POST.getlist('s_gripal')
	tempo_quadro_sintomatico = request.POST.get('tempo_inicio_sintomas')
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
	if spo2_cap != '':
		spo2 = int(spo2_cap)
	else:
		spo2 = None

	fr_irpm_cap = request.POST.get('fr_irpm')
	if fr_irpm_cap != '':
		fr_irpm = int(fr_irpm_cap)
	else:
		fr_irpm = None

	ventilacao_tipo = request.POST.get('ventilacao')
	o2_suporte = request.POST.getlist('o2_suporte')
	
	dose_cn_cap = request.POST.get('dose_cn')
	if dose_cn_cap != '':
		dose_cn = float(dose_cn_cap)
	else:
		dose_cn = None

	dose_venturi_cap = request.POST.get('dose_venturi')
	if dose_venturi_cap != '':
		dose_venturi = float(dose_venturi_cap)
	else:
		dose_venturi = None

	vmi = request.POST.getlist('vmi')
	
	vt_cap = request.POST.get('vt')
	if vt_cap != '':
		vt = float(vt_cap)
	else:
		vt = None

	delta_pressure_cap = request.POST.get('delta_pressure')
	if delta_pressure_cap != '':
		delta_pressure = float(delta_pressure_cap)
	else:
		delta_pressure = None

	pplato_cap = request.POST.get('pplato')
	if pplato_cap != '':
		pplato = float(pplato_cap)
	else:
		pplato = None

	raw_cap = request.POST.get('raw')
	if raw_cap != '':
		raw = float(raw_cap)
	else:
		raw = None

	cest_cap = request.POST.get('cest')
	if cest_cap != '':
		cest = float(cest_cap)
	else:
		cest = None

	sao2 = request.POST.get('sao2')
	pao2 = request.POST.get('pao2')
	fio2 = request.POST.get('fio2')
	paco2 = request.POST.get('paco2')
	
	fc_cap = request.POST.get('fc')
	if fc_cap != '':
		fc = int(fc_cap)
	else:
		fc = None

	temperatura_axilar_cap = request.POST.get('temp_auxiliar')
	if temperatura_axilar_cap != '':
		temperatura_axilar = float(temperatura_axilar_cap)
	else:
		temperatura_axilar = None

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
	data_coleta = request.POST.get('data_da_coleta')
	em_uso_corticosteroide = request.POST.get('em_uso_corticosteroide')
	dose_corticosteroide = request.POST.get('dose_corticosteroide')
	data_inicio_corticosteroide = request.POST.get('data_inicio_corticosteroide')
	em_uso_hidroxicloroquina = request.POST.get('em_uso_hidrocloroquina')
	data_inicio_hidroxicloroquina = request.POST.get('data_inicio_hidroxicloroquina')
	em_uso_oseltamivir = request.POST.get('em_uso_oseltamivir')
	data_inicio_oseltamivir = request.POST.get('data_inicio_oseltamivir')
	em_uso_heparina = request.POST.get('em_uso_heparina')
	data_inicio_heparina = request.POST.get('data_inicio_heparina')
	tipo_heparina = request.POST.get('tipo_heparina')
	dose_heparina = request.POST.get('dose_heparina')
	
	pps_cap = request.POST.get('pps_paciente')
	if pps_cap != '':
		pps = float(pps_cap)
	else:
		pps = None

	escala_pontos_glasgow_cap = request.POST.get('escala_glasgow')
	if escala_pontos_glasgow_cap != '':
		escala_pontos_glasgow = int(escala_pontos_glasgow_cap)
	else:
		escala_pontos_glasgow = None

	bloqueador_neuromuscular = request.POST.getlist('desc_bloqueador_neuromuscular')
	midazolam_dose = request.POST.get('midazolam_dose')
	fentanil_dose = request.POST.get('fentanil_dose')
	propofol_dose = request.POST.get('propofol_dose')
	sedacao_continua = request.POST.getlist('desc_sedacao_continua')
	rocuronio_dose = request.POST.get('rocuronio_dose')
	pacuronio_dose = request.POST.get('pacuronio_dose')
	cisatracurio_dose = request.POST.get('cisatracurio_dose')
	rass = request.POST.get('rass')
	data_exames_laboratorio = request.POST.get('data_exames_laboratorio')
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
	
	prioridade_cap = request.POST.get('prioridade')
	if prioridade_cap != '':
		prioridade = int(prioridade_cap)
	else:
		prioridade = None

	regulacao_paciente = request.POST.get('paciente_preenche_criterios')
	status_regulacao = request.POST.get('')
	codigo_sescovid = request.POST.get('num_protocolo')
	justificativa = request.POST.get('justificativa_nao_regulacao')
	observacao = request.POST.get('observacoes_medicas')
	pareceristas = request.POST.getlist('pareceristas')
	data_regulacao = request.POST.get('data_regulacao')

	
	registro.responsavel_pelo_preenchimento = responsavel_pelo_preenchimento
	registro.codigo_registro = codigo_registro
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
	registro.observacoes = observacoes
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
	registro.prioridade = prioridade
	registro.regulacao_paciente = regulacao_paciente
	registro.status_regulacao = status_regulacao
	registro.codigo_sescovid = codigo_sescovid
	registro.justificativa = justificativa
	registro.observacao = observacao
	registro.pareceristas = pareceristas
	registro.data_regulacao = data_regulacao

	registro.save()

	return redirect('regulacao_detail', id=id)


@login_required
def regulacao_detail(request, id):
	registro = RegistroCovid.objects.get(id=id)

	return render(request, 'regulacao_detail.html', {'registro':registro})

@login_required
def regulacao_edit(request, id):

	#registro_id = request.GET.get('id')
	#registro = RegistroCovid.objects.get(id=registro_id)
	registro = RegistroCovid.objects.get(id=id)
	pa = registro.pa

	if len(pa)>4:
		pa_1 = pa[0] + pa[1]
		pa_2 = pa[3] + pa[4]
	elif len(pa) == 4:
		pa_1 = pa[0] + pa[1]
		pa_2 = pa[3]
	else:
		pa_1 = ''
		pa_2 = ''

	return render(request, 'regulacao_edit.html', {'registro':registro, 'pa_1': pa_1, 'pa_2': pa_2})

@login_required
def regulacao_edit_set(request, id):

	registro = RegistroCovid.objects.get(id=id)

	responsavel_pelo_preenchimento = request.user
	
	codigo_registro = "20201"
	#implementar
	nome_solicitante = registro.nome_solicitante
	municipio_estabelecimento = registro.municipio_estabelecimento
	estabelecimento_solicitante = registro.estabelecimento_solicitante
	estabelecimento_outro = registro.estabelecimento_outro
	unidade_origem = registro.unidade_origem
	nome_paciente = request.POST.get('nome_paciente')
	idade_paciente = request.POST.get('idade_paciente')
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
	observacoes = registro.observacoes

	sindrome_gripal = request.POST.getlist('s_gripal')
	tempo_quadro_sintomatico = request.POST.get('tempo_inicio_sintomas')
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
	if spo2_cap != '':
		spo2 = int(spo2_cap)
	else:
		spo2 = None

	fr_irpm_cap = request.POST.get('fr_irpm')
	if fr_irpm_cap != '':
		fr_irpm = int(fr_irpm_cap)
	else:
		fr_irpm = None

	ventilacao_tipo = request.POST.get('ventilacao')
	o2_suporte = request.POST.getlist('o2_suporte')
	
	dose_cn_cap = request.POST.get('dose_cn')
	if dose_cn_cap != '':
		dose_cn = float(dose_cn_cap)
	else:
		dose_cn = None

	dose_venturi_cap = request.POST.get('dose_venturi')
	if dose_venturi_cap != '':
		dose_venturi = float(dose_venturi_cap)
	else:
		dose_venturi = None

	vmi = request.POST.getlist('vmi')
	
	vt_cap = request.POST.get('vt')
	if vt_cap != '':
		vt = float(vt_cap)
	else:
		vt = None

	delta_pressure_cap = request.POST.get('delta_pressure')
	if delta_pressure_cap != '':
		delta_pressure = float(delta_pressure_cap)
	else:
		delta_pressure = None

	pplato_cap = request.POST.get('pplato')
	if pplato_cap != '':
		pplato = float(pplato_cap)
	else:
		pplato = None

	raw_cap = request.POST.get('raw')
	if raw_cap != '':
		raw = float(raw_cap)
	else:
		raw = None

	cest_cap = request.POST.get('cest')
	if cest_cap != '':
		cest = float(cest_cap)
	else:
		cest = None

	sao2 = request.POST.get('sao2')
	pao2 = request.POST.get('pao2')
	fio2 = request.POST.get('fio2')
	paco2 = request.POST.get('paco2')
	
	fc_cap = request.POST.get('fc')
	if fc_cap != '':
		fc = int(fc_cap)
	else:
		fc = None

	temperatura_axilar_cap = request.POST.get('temp_auxiliar')
	if temperatura_axilar_cap != '':
		temperatura_axilar = float(temperatura_axilar_cap)
	else:
		temperatura_axilar = None

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
	
	data_coleta_cap = request.POST.get('data_da_coleta')
	data_coleta = datetime.strptime(data_coleta_cap, '%d/%m/%Y').date()
	
	em_uso_corticosteroide = request.POST.get('em_uso_corticosteroide')
	dose_corticosteroide = request.POST.get('dose_corticosteroide')
	data_inicio_corticosteroide = request.POST.get('data_inicio_corticosteroide')
	em_uso_hidroxicloroquina = request.POST.get('em_uso_hidrocloroquina')
	data_inicio_hidroxicloroquina = request.POST.get('data_inicio_hidroxicloroquina')
	em_uso_oseltamivir = request.POST.get('em_uso_oseltamivir')
	data_inicio_oseltamivir = request.POST.get('data_inicio_oseltamivir')
	em_uso_heparina = request.POST.get('em_uso_heparina')
	data_inicio_heparina = request.POST.get('data_inicio_heparina')
	tipo_heparina = request.POST.get('tipo_heparina')
	dose_heparina = request.POST.get('dose_heparina')
	
	pps_cap = request.POST.get('pps_paciente')
	if pps_cap != '':
		pps = float(pps_cap)
	else:
		pps = None

	escala_pontos_glasgow_cap = request.POST.get('escala_glasgow')
	if escala_pontos_glasgow_cap != '':
		escala_pontos_glasgow = int(escala_pontos_glasgow_cap)
	else:
		escala_pontos_glasgow = None

	bloqueador_neuromuscular = request.POST.getlist('desc_bloqueador_neuromuscular')
	midazolam_dose = request.POST.get('midazolam_dose')
	fentanil_dose = request.POST.get('fentanil_dose')
	propofol_dose = request.POST.get('propofol_dose')
	sedacao_continua = request.POST.getlist('desc_sedacao_continua')
	rocuronio_dose = request.POST.get('rocuronio_dose')
	pacuronio_dose = request.POST.get('pacuronio_dose')
	cisatracurio_dose = request.POST.get('cisatracurio_dose')
	rass = request.POST.get('rass')
	data_exames_laboratorio = request.POST.get('data_exames_laboratorio')
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
	
	prioridade_cap = request.POST.get('prioridade')
	if prioridade_cap != '':
		prioridade = int(prioridade_cap)
	else:
		prioridade = None

	regulacao_paciente = request.POST.get('paciente_preenche_criterios')
	status_regulacao = request.POST.get('')
	codigo_sescovid = request.POST.get('num_protocolo')
	justificativa = request.POST.get('justificativa_nao_regulacao')
	observacao = request.POST.get('observacoes_medicas')
	pareceristas = request.POST.getlist('pareceristas')
	data_regulacao = request.POST.get('data_regulacao')

	
	registro.responsavel_pelo_preenchimento = responsavel_pelo_preenchimento
	registro.codigo_registro = codigo_registro
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
	registro.observacoes = observacoes
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
	registro.prioridade = prioridade
	registro.regulacao_paciente = regulacao_paciente
	registro.status_regulacao = status_regulacao
	registro.codigo_sescovid = codigo_sescovid
	registro.justificativa = justificativa
	registro.observacao = observacao
	registro.pareceristas = pareceristas
	registro.data_regulacao = data_regulacao

	registro.save()

	return redirect('covid_list')
