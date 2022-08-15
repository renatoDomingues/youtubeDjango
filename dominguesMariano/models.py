# Create your models here.

from django.db import models

#Criar uma classe com um nome de um metodo da mesma, para depois adcionarmos os atributos:
class ConsultarProdutos(models.Model):
    #para podermos adcionarmos o nome
    nome_completo=models.CharField(max_length=256)
    #Vai permitir dataNascimento poderá ser null
    data_nascimento=models.DateField(null=True)
    #para saber se a pessoa está ativa ou não
    ativa=models.BooleanField(default=True)

#Depois vamos para o desenvolvimento pessoa/views.py
