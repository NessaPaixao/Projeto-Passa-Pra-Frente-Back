from django.db import models

# Create your models here.

class Escola(models.Model):

    nome_responsavel = models.CharField(
        max_length=100, verbose_name='Nome_responsavel')

    cpf_responsavel = models.IntegerField(
        verbose_name='Cpf_responsavel')

    nome_escola = models.CharField(
        max_length=100, verbose_name='Nome_escola')

    cep = models.IntegerField(
        verbose_name='cep')

    telefone = models.CharField(
        max_length=255, verbose_name='telefone')

    usuario= models.CharField(
        max_length=255, verbose_name='usuario')

    senha = models.CharField(
        max_length=255, verbose_name='senha')

    def __str__(self):
        return self.nome_escola


