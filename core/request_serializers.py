from rest_framework import serializers
from core.models import Transacao


class TransacaoCreateUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer focado em Escrita (POST/PUT/PATCH).
    Recebe IDs simples para relacionamentos.
    """

    class Meta:
        model = Transacao
        fields = [
            'descricao', 'valor', 'data',
            'categoria', 'usuario', 'conta_bancaria', 'cartao'
        ]

    def validate_valor(self, value):
        """
        Exemplo de boa prática: Validar se o valor não é zero.
        """
        if value == 0:
            raise serializers.ValidationError("O valor da transação não pode ser zero.")
        return value

    def validate(self, data):
        """
        Validação cruzada: Uma transação deve ter ou uma conta bancária ou um cartão.
        """
        if not data.get('conta_bancaria') and not data.get('cartao'):
            raise serializers.ValidationError(
                "A transação deve estar vinculada a uma conta bancária ou a um cartão de crédito."
            )
        return data