from django.db import models

# Create your models here.
from Escola.models import Escola
from doador.models import Doador


class Doacao(models.Model):

    nome = models.CharField(
        max_length=50, verbose_name='Nome_doacao')

    quantidade = models.IntegerField(
        verbose_name='quantidade')

    descricao = models.CharField(
        max_length=255, verbose_name='descricao')

    doador = models.ForeignKey(Doador, on_delete=models.SET_NULL, null=True)
    escola = models.ForeignKey(Escola, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome__

