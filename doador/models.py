from django.db import models

# Create your models here.

class Doador(models.Model):

    nome = models.CharField(
        max_length=50,
        verbose_name='Nome_doador',
    )

    idade = models.IntegerField(
        verbose_name='idade'
    )

    cpf = models.IntegerField(
        verbose_name='cpf'
    )

    email = models.CharField(
        max_length=255,
        verbose_name='email'
    )

    senha = models.CharField(
        max_length=255,
        verbose_name='senha'
    )

    cep = models.IntegerField(
        verbose_name='cep'
    )

    def __str__(self):
        return self.nome
