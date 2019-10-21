from django.shortcuts import render

from rest_framework import viewsets
from Escola.models import Escola
from Escola.serializers import EscolaSerializer


class EscolaViewSet(viewsets.ModelViewSet):
    queryset = Escola.objects.all()
    serializer_class = EscolaSerializer