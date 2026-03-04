from django.contrib import admin
from .models import Usuario, Banco, ContaBancaria, CartaoDeCredito, Categoria, Transacao

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'is_active')

@admin.register(Banco)
class BancoAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(ContaBancaria)
class ContaBancariaAdmin(admin.ModelAdmin):
    list_display = ('banco', 'usuario', 'valor')

@admin.register(CartaoDeCredito)
class CartaoDeCreditoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'bandeira', 'limite')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo')

@admin.register(Transacao)
class TransacaoAdmin(admin.ModelAdmin):
    # Note que aqui só temos 3 itens no list_filter. O erro dizia que o erro estava no item [3] (o quarto item).
    list_display = ('descricao', 'valor', 'data', 'categoria', 'usuario')
    list_filter = ('data', 'categoria', 'usuario')
    search_fields = ('descricao',)