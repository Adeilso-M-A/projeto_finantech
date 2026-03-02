from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.viewsets import UsuarioViewSet, CategoriaViewSet, TransacaoViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuario')
router.register(r'categorias', CategoriaViewSet, basename='categoria')
router.register(r'transacoes', TransacaoViewSet, basename='transacao')

urlpatterns = [
    path('', include(router.urls)),
]