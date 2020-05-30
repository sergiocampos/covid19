from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime, timezone

# Create your views here.

@login_required
def covid_list(request):
	return render(request, 'list.html')


@login_required
def registro_covid(request):
	data = datetime.now()
	formateDate = data.strftime("%d-%m-%Y")
	hora = data.strftime("%H:%M")

	num_part_1 = '1209'
	num_part_2 = '1209'

	num_registro = num_part_1 + num_part_2



	print("data:", formateDate)
	print("data:", hora)
	return render(request, 'registro_covid.html', {'formateDate': formateDate, 'hora': hora, 'num_registro':num_registro})


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
	nome_paciente = request.POST.get('nome_paciente')
	idade_paciente = request.POST.get('idade_paciente')
	unidade_origem = request.POST.get('unidade_origem')
	recurso_que_precisa = request.POSt.get('recurso_que_precisa')
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

	print("passou no set covid!")

	#implementar o algoritmo: codigo_registro = None

	registro = RegistroCovid.objects.create(
		nome_solicitante = nome_solicitante,
		municipio_estabelecimento = municipio_estabelecimento,
		estabelecimento_solicitante = estabelecimento_solicitante,
		estabelecimento_outro = estabelecimento_outro,
		unidade_origem = unidade_origem,
		nome_paciente = nome_paciente,
		idade_paciente = idade_paciente,

		responsavel_pelo_preenchimento = responsavel_pelo_preenchimento)





	


	return redirect('covid_list')

@login_required
def registro_enfermeiro_medico(request):
    return render(request, 'registro_enfermeiro_medico.html')

@login_required
def regulacao(request):
    return render(request, 'regulacao.html')

@login_required
def regulacao_edit(request):

	return render(request, 'regulacao_edit.html')
