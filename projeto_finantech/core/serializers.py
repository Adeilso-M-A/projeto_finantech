from rest_framework import serializers
from core.models import Usuario, Banco, ContaBancaria, CartaoDeCredito, Categoria, Transacao

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'email', 'is_active', 'created_at']

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nome', 'tipo']

class TransacaoDetailSerializer(serializers.ModelSerializer):
    """Serializer para GET - Mostra detalhes aninhados"""
    categoria_detalhe = CategoriaSerializer(source='categoria', read_only=True)
    usuario_nome = serializers.ReadOnlyField(source='usuario.nome')

    class Meta:
        model = Transacao
        fields = [
            'id', 'descricao', 'valor', 'data',
            'categoria', 'categoria_detalhe',
            'usuario', 'usuario_nome',
            'conta_bancaria', 'cartao'
        ]