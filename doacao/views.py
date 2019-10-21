from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from doacao.models import Doacao
from doacao.serializers import DoacaoSerializer


class DoacaoViewSet(viewsets.ModelViewSet):
    queryset = Doacao.objects.all()
    serializer_class = DoacaoSerializer