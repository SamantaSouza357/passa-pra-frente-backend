from django.shortcuts import render
from rest_framework import viewsets
from Doacao.models import Doacao
from Doacao.serializers import DoacaoSerializer


class DoacaoViewSet(viewsets.ModelViewSet):
    queryset = Doacao.objects.all()
    serializer_class = DoacaoSerializer

