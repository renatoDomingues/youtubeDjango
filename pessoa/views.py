# Create your views here.

from django.shortcuts import render
#Esse ListView abaixo, um beneficio Django nos fornece classe, desenvolver na tela
from django.views.generic import ListView
from .models import Pessoa

class ListaPessoaView(ListView):
    model=Pessoa
    #trago todas dentro da Pessoa
    queryset=Pessoa.objects.all().order_by('nome_completo')

#Depois devemos criar um urls
