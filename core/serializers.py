from rest_framework import serializers
from core.models import Usuario, Banco, ContaBancaria, CartaoDeCredito, Categoria, Transacao


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'email', 'is_active', 'created_at']


class CategoriaSerializer(serializers.ModelSerializer):
    # Mostra o texto amigável (Receita/Despesa) em vez do código interno
    tipo_display = serializers.CharField(source='get_tipo_display', read_only=True)

    class Meta:
        model = Categoria
        fields = ['id', 'nome', 'tipo', 'tipo_display']


class TransacaoDetailSerializer(serializers.ModelSerializer):
    """Serializer para GET - Focado em leitura (Read)"""
    # Retorna o objeto completo da categoria
    categoria = CategoriaSerializer(read_only=True)

    # Atalhos para nomes de campos relacionados (evita IDs puros no frontend)
    usuario_nome = serializers.ReadOnlyField(source='usuario.nome')
    banco_nome = serializers.ReadOnlyField(source='conta_bancaria.banco.nome')
    cartao_nome = serializers.ReadOnlyField(source='cartao.nome')

    class Meta:
        model = Transacao
        fields = [
            'id', 'descricao', 'valor', 'data',
            'categoria', 'usuario_nome',
            'banco_nome', 'cartao_nome', 'is_active'
        ]


class BancoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banco
        fields = ['id', 'nome', 'usuario']


class ContaBancariaSerializer(serializers.ModelSerializer):
    banco_nome = serializers.ReadOnlyField(source='banco.nome')

    class Meta:
        model = ContaBancaria
        fields = ['id', 'valor', 'banco', 'banco_nome', 'usuario', 'is_active']


class CartaoDeCreditoSerializer(serializers.ModelSerializer):
    banco_nome = serializers.ReadOnlyField(source='banco.nome')

    class Meta:
        model = CartaoDeCredito
        fields = ['id', 'nome', 'bandeira', 'numero', 'limite', 'banco', 'banco_nome', 'usuario']