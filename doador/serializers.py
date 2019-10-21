from rest_framework import serializers
from doador.models import Doador


class DoadorSerializer(serializerModelSerializer):
    class Meta:
        model = Doador
        fields = ('nome','id','idade','cpf','email','senha')