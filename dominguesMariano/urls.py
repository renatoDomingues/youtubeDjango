
# Create your views here.

#from django.shortcuts import render
from django.urls import path
from .views import ConsultarProdutos

urlpatterns = [
    #1° parametro da listagem, acostumamos deixar vazio, o 2° buscarmos na importação acima e o ultimo o nome da nossa rota
    path('', ConsultarProdutos.as_view(), name='DominguesMariano')
]

#Irmos para 'project/settings.py', na 'INSTALLED_APPS =' para adcionarmos os novos app que desenvolvermos no
