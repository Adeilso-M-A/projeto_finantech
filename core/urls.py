from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.viewsets import (
    UsuarioViewSet, CategoriaViewSet, TransacaoViewSet,
    BancoViewSet, ContaBancariaViewSet, CartaoDeCreditoViewSet
)

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuario')
router.register(r'categorias', CategoriaViewSet, basename='categoria')
router.register(r'transacoes', TransacaoViewSet, basename='transacao')
router.register(r'bancos', BancoViewSet, basename='banco')
# Ajustado para nomes mais claros e padronizados:
router.register(r'contas-bancarias', ContaBancariaViewSet, basename='contas-bancarias')
router.register(r'cartoes-credito', CartaoDeCreditoViewSet, basename='cartoes-credito')

urlpatterns = [
    path('', include(router.urls)),
]