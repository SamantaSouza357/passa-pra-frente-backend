from rest_framework import serializers
from Doacao.models import Doacao


class DoacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doacao
        fields = ['id','nome','descricao','quantidade']