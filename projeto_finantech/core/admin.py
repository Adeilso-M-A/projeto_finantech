from django.contrib import admin
from core.models import Usuario, Banco, ContaBancaria, CartaoDeCredito, Categoria, Transacao

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'created_at', 'is_active')
    search_fields = ('nome', 'email')

@admin.register(Banco)
class BancoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'usuario', 'created_at')
    list_filter = ('usuario',)

@admin.register(ContaBancaria)
class ContaBancariaAdmin(admin.ModelAdmin):
    list_display = ('banco', 'usuario', 'valor', 'is_active')
    list_filter = ('usuario', 'banco')

@admin.register(CartaoDeCredito)
class CartaoDeCreditoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'bandeira', 'usuario', 'limite')
    search_fields = ('nome', 'numero')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'usuario')
    list_filter = ('tipo', 'usuario')

@admin.register(Transacao)
class TransacaoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'valor', 'data', 'categoria', 'usuario')
    list_filter = {'data', 'categoria', 'usuario', 'tipo_transacao'}  # Se adicionar tipo no modelo
    search_fields = ('descricao',)