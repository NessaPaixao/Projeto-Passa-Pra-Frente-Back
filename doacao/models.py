from django.db import models

# Create your models here.

class Doacao(models.Model):

    nome = models.CharField(
        max_length=50, verbose_name='Nome_doacao')

    quantidade = models.IntegerField(
        verbose_name='quantidade')

    descricao = models.CharField(
        max_length=255,
        verbose_name='descricao'
    )


