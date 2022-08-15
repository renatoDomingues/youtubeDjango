
from django.urls import path
from .views import ListaPessoaView

urlpatterns = [
    #1° parametro da listagem, acostumamos deixar vazio, o 2° buscarmos na importação acima e o ultimo o nome da nossa rota
    path('', ListaPessoaView.as_view(), name='pessoa.index')
]

#Irmos para 'project/settings.py', na 'INSTALLED_APPS =' para adcionarmos os novos app que desenvolvermos no