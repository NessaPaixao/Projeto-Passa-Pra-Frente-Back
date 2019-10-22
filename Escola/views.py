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

    