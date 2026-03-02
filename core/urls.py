from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.viewsets import UsuarioViewSet, CategoriaViewSet, TransacaoViewSet, BancoViewSet, ContaBancariaViewSet, \
    CartaoDeCreditoViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuario')
router.register(r'categorias', CategoriaViewSet, basename='categoria')
router.register(r'transacoes', TransacaoViewSet, basename='transacao')
router.register(r'bancos', BancoViewSet, basename='banco')
router.register(r'contas', ContaBancariaViewSet, basename='contas')
router.register(r'cartoes', CartaoDeCreditoViewSet, basename='cartaodes')

urlpatterns = [
    path('', include(router.urls)),
]