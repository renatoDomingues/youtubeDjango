# Create your models here.

from django.db import models

#Criar uma classe com um nome de um metodo da mesma, para depois adcionarmos os atributos:
class Produtos(models.Model):
    #para podermos adcionarmos o nome
    nome_produto = models.CharField(max_length=256)
    #codigo de barra do produto
    codigo_barra = models.CharField(max_length=14)
    #preço do produto
    preco_produto = models.DecimalField(max_digits=4, decimal_places=2)
    #Vai permitir dataNascimento poderá ser null
    data_vencimento = models.DateField(null=True)

#Depois vamos para o desenvolvimento pessoa/views.py
