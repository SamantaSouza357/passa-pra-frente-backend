from rest_framework import serializers
from Escola.models import Escola


class EscolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escola
        fields = ['id','nome','email','telefone','endereco','senha']