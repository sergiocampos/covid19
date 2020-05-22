from django.urls import path
from . import views

urlpatterns = [
	path('', views.covid_list, name='covid_list'),

]