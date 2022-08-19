# Create your views here.

from django.shortcuts import render
#Esse ListView abaixo, um beneficio Django nos fornece classe, desenvolver na tela
from django.views.generic import ListView, CreateView
from .models import Pessoa
from .forms import PessoaForm

class ListaPessoaView(ListView):
    model = Pessoa
    #trago todas dentro da Pessoa
    queryset = Pessoa.objects.all().order_by('nome_completo')

#Depois devemos criar um urls

class PessoaCreateView(CreateView):
    model = Pessoa
    form_class = PessoaForm
    success_url = '/pessoas/'
    
#Depois vai na urls.py
