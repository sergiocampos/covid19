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
from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('covid_list/', views.covid_list, name='covid_list'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registro_covid/', views.registro_covid, name='registro_covid'),
    path('registro_covid/submit', views.registro_covid_set),
    path('registro_enfermeiro_medico/', views.registro_enfermeiro_medico, name='registro_enfermeiro_medico'),
    path('regulacao/<id>/', views.regulacao, name='regulacao'),
    path('regulacao/<id>/submit', views.regulacao_set),
    path('regulacao_edit/<id>/', views.regulacao_edit, name='regulacao_edit'),
    path('regulacao_edit/<id>/submit', views.regulacao_edit_set),
    path('regulacao_detail/<id>/', views.regulacao_detail, name='regulacao_detail' )
]
