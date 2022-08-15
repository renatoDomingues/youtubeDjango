#Depois desenvolvermos a pasta 'template/main' com arquivo 'index.html' e junto coda no arquivo já existente por python manage.py startapp main 'views.py':

from django.urls import path
from .views import HomeView

#Informar os padrões da urls, com o nome do metodo da classe e por 3° parametro/ultimo o nome que só dev saberá:
urlpatterns = [
    path('', HomeView.as_view(), name='home')
]
