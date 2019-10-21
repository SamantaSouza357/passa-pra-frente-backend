from django.shortcuts import render
from rest_framework import viewsets
from Doador.models import Doador
from Doador.serializers import DoadorSerializer


class DoadorViewSet(viewsets.ModelViewSet):
    queryset = Doador.objects.all()
    serializer_class = DoadorSerializer
