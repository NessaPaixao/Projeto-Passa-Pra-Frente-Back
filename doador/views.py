from django.shortcuts import render
from rest_framework import viewsets
from doador.models import Doador
from doador.serializers import DoadorSerializer


class DoadorViewSet(viewsets.ModelViewSet):
    queryset = Doador.objects.all()
    serializer_class = DoadorSerializer
