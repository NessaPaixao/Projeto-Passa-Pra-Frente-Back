from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from Escola.models import Escola
from Escola.serializers import EscolaSerializer
from doacao.models import Doacao
from doacao.serializers import DoacaoSerializer


class EscolaViewSet(viewsets.ModelViewSet):
    queryset = Escola.objects.all()
    serializer_class = EscolaSerializer

    @action(detail=True, methods=['POST'])
    def aceitar(self, request, pk=None):
        doacao = Doacao.objects.get(pk=request.data['doacao'])
        doacao.escola = self.get_object()
        # doacao.escola = None
        doacao.save(update_fields=["escola"])
        return Response({'messege': 'doado!'})

    @action(detail=True, methods=["POST"])
    def cancelar(self, request, pk=None):
        doacao = Doacao.objects.get(pk=request.data['doacao'])
        doacao.escola = None
        doacao.save(update_fields=["escola"])
        return Response({'messege': 'Cancelado a doação'})

    @action(detail=True, methods=["GET"])
    def aceitados(self, request, pk=None):
        doacao = Doacao.objects.all().filter(escola=pk)
        return Response(DoacaoSerializer(doacao, many=True).data)