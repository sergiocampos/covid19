from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def covid_list(request):
	return render(request, 'list.html')


@login_required
def registro_covid(request):
    
    return render(request, 'registro_covid.html')


@login_required
def registro_enfermeiro_medico(request):
    return render(request, 'registro_enfermeiro_medico.html')

@login_required
def regulacao(request):
    return render(request, 'regulacao.html')

@login_required
def registro_covid_set(request):
        
    return redirect('registro_covid_all')