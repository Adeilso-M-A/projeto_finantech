from rest_framework import serializers
from core.models import Transacao, ContaBancaria, CartaoDeCredito

class TransacaoCreateUpdateSerializer(serializers.ModelSerializer):
    """Serializer para POST/PUT - Focado em receber IDs"""
    class Meta:
        model = Transacao
        fields = [
            'descricao', 'valor', 'data',
            'categoria', 'usuario',
            'conta_bancaria', 'cartao'
        ]

    def validate_valor(self, value):
        if value <= 0:
            raise serializers.ValidationError("O valor da transação deve ser maior que zero.")
        return value