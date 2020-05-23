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
	return render(request, 'registro_covid.html', {'formateDate': formateDate, 'hora': hora})


@login_required
def registro_covid_set(request):
	user = request.user

	nome_solicitante = request.POST.get('nome_solicitante')

	return redirect('covid_list')

@login_required
def registro_enfermeiro_medico(request):
    return render(request, 'registro_enfermeiro_medico.html')

@login_required
def regulacao(request):
    return render(request, 'regulacao.html')

@login_required
def registro_covid_set(request):
        
    return redirect('registro_covid_all')