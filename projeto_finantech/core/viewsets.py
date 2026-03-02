from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from core.models import Usuario, Categoria, Transacao, Banco, ContaBancaria, CartaoDeCredito
from core.serializers import UsuarioSerializer, CategoriaSerializer, TransacaoDetailSerializer
from core.request_serializers import TransacaoCreateUpdateSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.filter(is_active=True)
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny]

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.filter(is_active=True)
    serializer_class = CategoriaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tipo', 'usuario']

class TransacaoViewSet(viewsets.ModelViewSet):
    """
    ViewSet que utiliza a lógica de separação de serializers do guia.
    """
    queryset = Transacao.objects.filter(is_active=True).select_related('categoria', 'usuario')
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['categoria', 'usuario', 'data']
    search_fields = ['descricao']
    ordering = ['-data']

    def get_serializer_class(self):
        # Se for criação ou edição, usa o serializer de escrita (request_serializers.py)
        if self.action in ['create', 'update', 'partial_update']:
            return TransacaoCreateUpdateSerializer
        # Para listagem e detalhes, usa o serializer de leitura (serializers.py)
        return TransacaoDetailSerializer

    def perform_destroy(self, instance):
        # Implementação de Soft Delete conforme sugerido no guia
        instance.is_active = False
        instance.save()