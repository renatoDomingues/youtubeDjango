
from django.urls import path
from .views import ListaPessoaView, PessoaCreateView, PessoaUpdateView, PessoaDeleteView

urlpatterns = [
    #1° parametro da listagem, acostumamos deixar vazio, o 2° buscarmos na importação acima e o ultimo o nome da nossa rota
    path('', ListaPessoaView.as_view(), name='pessoa.index'),
    path('novo/', PessoaCreateView.as_view(), name='pessoa.novo'),
    
    #path('editar/<int:id>', PessoaUpdateView.as_view(), name='pessoa.editar')
    
    path('editar/<int:pk>', PessoaUpdateView.as_view(), name='pessoa.editar'),
    path('remover/<int:pk>', PessoaDeleteView.as_view(), name='pessoa.remover')
    
    #Depois essa "path editar" do UPDATE, necessita chamar na pessoa_list
]

#Irmos para 'project/settings.py', na 'INSTALLED_APPS =' para adcionarmos os novos app que desenvolvermos no
