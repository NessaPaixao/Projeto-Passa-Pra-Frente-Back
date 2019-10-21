from Escola.models import Escola
from doador import serializers


class EscolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escola
        fields = ('id','nome_resposanvel','cpf_responsavel', 'nome_escola', 'cep', 'telefone', 'usuario','senha')