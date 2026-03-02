from django.db import models
import uuid


class BaseModel(models.Model):
    """Modelo base seguindo o guia para padronização"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Usuario(BaseModel):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    senha = models.CharField(max_length=100)

    # data_criacao já está no BaseModel como created_at

    def __str__(self):
        return self.nome


class Banco(BaseModel):
    nome = models.CharField(max_length=100)  # Representando a coluna de identificação do banco
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='bancos')

    def __str__(self):
        return self.nome


class ContaBancaria(BaseModel):
    valor = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    banco = models.ForeignKey(Banco, on_delete=models.CASCADE, related_name='contas')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='contas_bancarias')

    class Meta:
        verbose_name_plural = "Contas Bancárias"


class CartaoDeCredito(BaseModel):
    nome = models.CharField(max_length=40)
    bandeira = models.CharField(max_length=40)
    numero = models.CharField(max_length=40)
    limite = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)  # valor no diagrama
    banco = models.ForeignKey(Banco, on_delete=models.CASCADE, related_name='cartoes')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='cartoes')

    class Meta:
        verbose_name_plural = "Cartões de Crédito"


class Categoria(BaseModel):
    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=10)  # Ex: Receita/Despesa
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='categorias')

    def __str__(self):
        return self.nome


class Transacao(BaseModel):
    descricao = models.CharField(max_length=128)
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    data = models.DateTimeField()

    # Chaves Estrangeiras conforme o diagrama
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='transacoes')
    conta_bancaria = models.ForeignKey(ContaBancaria, on_delete=models.CASCADE, related_name='transacoes', null=True,
                                       blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='transacoes')
    cartao = models.ForeignKey(CartaoDeCredito, on_delete=models.SET_NULL, related_name='transacoes', null=True,
                               blank=True)

    class Meta:
        verbose_name_plural = "Transações"
        ordering = ['-data']

    def __str__(self):
        return f"{self.descricao} - {self.valor}"