from django.conf.urls import url
from Ontoapp import views

urlpatterns = [
    url(r'^projet/$', views.page),
	url(r'^upload/$', views.Upload),
]