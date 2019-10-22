from rest_framework import serializers
from Escola.models import Escola


class EscolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escola
        fields = ('id','nome_responsavel','cpf_responsavel', 'nome_escola', 'cep', 'telefone', 'usuario','senha')

