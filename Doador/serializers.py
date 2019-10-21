from rest_framework import serializers
from Doador.models import Doador


class DoadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doador
        fields = ['id','nome','email','telefone','endereco','senha']