from rest_framework import serializers
from doacao.models import Doacao


class DoacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doacao
        fields = ('nome','id','quantidade','descriçao')