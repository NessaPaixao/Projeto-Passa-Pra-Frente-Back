from rest_framework import serializers
from doador.models import Doador


class DoadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doador
        fields = ('id','nome','idade','cep','cpf','email','senha')