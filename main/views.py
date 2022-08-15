# Create your views here.

from django.shortcuts import render
from django.views.generic import TemplateView

#Criar uma classe, e dar nome do metodo:
class HomeView(TemplateView):
    #INformar um parametro a onde a mesma tem que renderizar
    template_name='main/index.html'
    #template_name='main/dominguesMariano.html'
