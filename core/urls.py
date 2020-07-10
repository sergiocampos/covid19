from django.urls import path
from . import views
from django.conf.urls import url
from core import views

app_name = 'core'

urlpatterns = [
	path('', views.covid_list, name='covid_list'),
	url(r'^register/$',views.register,name='register'),
	url(r'^user_login/$',views.user_login,name='user_login'),
]