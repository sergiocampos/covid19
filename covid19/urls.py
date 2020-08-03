"""covid19 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    #url(r'^password/$', views.change_password, name='change_password'),
    
    url(r'^$',views.index,name='index'),
    url(r'^special/',views.special,name='special'),
    url(r'^core/',include('core.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),

    path('change_password/', views.change_password, name='change_password'),

    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('covid_list/', views.covid_list, name='covid_list'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    path('search_estabelecimento/', views.search_estabelecimento, name='search_estabelecimento'),
    path('search_estabelecimento/submit', views.search_estabelecimento_set),
    path('registro_covid/', views.registro_covid, name='registro_covid'),
    path('registro_covid/submit', views.registro_covid_set),
    path('registro_enfermeiro_medico/', views.registro_enfermeiro_medico, name='registro_enfermeiro_medico'),
    path('regulacao/<id>/', views.regulacao, name='regulacao'),
    path('regulacao/<id>/submit', views.regulacao_set),
    path('regulacao_edit/<id>/', views.regulacao_edit, name='regulacao_edit'),
    path('regulacao_edit/<id>/submit', views.regulacao_edit_set),
    path('regulacao_detail/<id>/', views.regulacao_detail, name='regulacao_detail' ),
    path('regulacao_search_estabelecimento/<id>/', views.regulacao_search_estabelecimento, name='regulacao_search_estabelecimento' ),
    path('regulacao_search_estabelecimento/<id>/submit', views.regulacao_search_estabelecimento_set),
    path('search_register/', views.search_register, name='search_register'),
    path('search_between_date/', views.search_between_date, name='search_between_date'),
    path('search_between_date/submit', views.search_between_date_set),
    path('result_search_between_date/', views.result_search_between_date, name='result_search_between_date'),
    path('gerar_relatorios/', views.gerar_relatorios, name='gerar_relatorios'),
    path('gerar_relatorios/submit', views.gerar_relatorios_set),
    path('result_for_relatorios/', views.result_for_relatorios, name='result_for_relatorios'),
    path('status_registro/<id>/', views.status_registro, name='status_registro'),
    path('status_registro/<id>/submit', views.status_registro_set),
    path('remove_registro_covid/<id>/', views.remove_registro_covid, name='remove_registro_covid'),
    path('image_descricao_clinica_alter/<id>/', views.image_descricao_clinica_alter, name='image_descricao_clinica_alter'),
    path('image_descricao_clinica_alter/<id>/submit', views.image_descricao_clinica_alter_set),
    path('image_rx_torax_alter/<id>/', views.image_rx_torax_alter, name='image_rx_torax_alter'),
    path('image_rx_torax_alter/<id>/submit', views.image_rx_torax_alter_set),
    path('image_tc_torax_alter/<id>/', views.image_tc_torax_alter, name='image_tc_torax_alter'),
    path('image_tc_torax_alter/<id>/submit', views.image_tc_torax_alter_set),
    path('regular_registro/<id>/', views.regular_registro, name='regular_registro'),
    path('regular_registro/<id>/submit', views.regular_registro_set),
    path('paciente_atribuir_senha/<id>/', views.paciente_atribuir_senha, name='paciente_atribuir_senha'),
    path('paciente_atribuir_senha/<id>/submit', views.paciente_atribuir_senha_set),
    path('template_censo/', views.template_censo, name='template_censo')
]
