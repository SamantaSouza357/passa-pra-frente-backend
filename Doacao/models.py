from django.db import models


class Doacao(models.Model):
    nome = models.CharField(max_length=255)
    quantidade = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)