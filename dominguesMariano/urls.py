
# Create your views here.

#from django.shortcuts import render
from django.urls import path
from .views import ConsultarProdutos

urlpatterns = [
    #1° parametro da listagem, acostumamos deixar vazio, o 2° buscarmos na importação acima e o ultimo o nome da nossa rota
    path('produtos', ConsultarProdutos.as_view(), name='produtos.index')
]

#from django.urls import path
#from .views import ListaPessoaView, PessoaCreateView, PessoaUpdateView
#urlpatterns = [
    #1° parametro da listagem, acostumamos deixar vazio, o 2° buscarmos na importação acima e o ultimo o nome da nossa rota
#    path('', ListaPessoaView.as_view(), name='pessoa.index'),
#    path('novo/', PessoaCreateView.as_view(), name='pessoa.novo'),
#    path('editar/<int:id>', PessoaUpdateView.as_view(), name='pessoa.editar')
    #Depois essa "path editar" do UPDATE, necessita chamar na pessoa_list
#]
#Irmos para 'project/settings.py', na 'INSTALLED_APPS =' para adcionarmos os novos app que desenvolvermos no
