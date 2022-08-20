
# Create your views here.

from django.shortcuts import render
#Esse ListView abaixo, um beneficio Django nos fornece classe, desenvolver na tela
from django.views.generic import ListView
from .models import Produtos

class ConsultarProdutos(ListView):
    model = Produtos
    #trago todas dentro da Pessoa
    queryset = Produtos.objects.all().order_by('nome_produto')

#Depois devemos criar um urls
