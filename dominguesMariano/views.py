
# Create your views here.

from django.shortcuts import render
#Esse ListView abaixo, um beneficio Django nos fornece classe, desenvolver na tela
from django.views.generic import ListView
from .models import dominguesMariano

class ConsultarProdutos(ListView):
    model=dominguesMariano
    #trago todas dentro da Pessoa
    queryset=dominguesMariano.objects.all().order_by('nome_completo')

#Depois devemos criar um urls
