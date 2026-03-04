from django.db import models
import uuid

class BaseModel(models.Model):
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

    def __str__(self):
        return self.nome

class Banco(BaseModel):
    nome = models.CharField("Nome do Banco", max_length=100)
    usuario = models.ForeignKey(Usuario, on_delete=models.RESTRICT, related_name='bancos')

    def __str__(self):
        return self.nome

class ContaBancaria(BaseModel):
    valor = models.DecimalField("Saldo Atual", max_digits=12, decimal_places=2, default=0.00)
    banco = models.ForeignKey(Banco, on_delete=models.RESTRICT, related_name='contas')
    usuario = models.ForeignKey(Usuario, on_delete=models.RESTRICT, related_name='contas_bancarias')

    class Meta:
        verbose_name_plural = "Contas Bancárias"

    def __str__(self):
        return f"{self.banco.nome} - {self.usuario.nome}"

class CartaoDeCredito(BaseModel):
    nome = models.CharField(max_length=40)
    bandeira = models.CharField(max_length=40)
    numero = models.CharField(max_length=40)
    limite = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    banco = models.ForeignKey(Banco, on_delete=models.RESTRICT, related_name='cartoes')
    usuario = models.ForeignKey(Usuario, on_delete=models.RESTRICT, related_name='cartoes_credito')

    class Meta:
        verbose_name_plural = "Cartões de Crédito"

    def __str__(self):
        return f"{self.nome} - {self.bandeira}"

class Categoria(BaseModel):
    class TipoChoices(models.TextChoices):
        RECEITA = 'RECEITA', 'Receita'
        DESPESA = 'DESPESA', 'Despesa'

    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=10, choices=TipoChoices.choices, default=TipoChoices.DESPESA)
    usuario = models.ForeignKey(Usuario, on_delete=models.RESTRICT, related_name='categorias')

    def __str__(self):
        return f"{self.nome} ({self.get_tipo_display()})"

class Transacao(BaseModel):
    descricao = models.CharField(max_length=128)
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    data = models.DateTimeField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='transacoes')
    conta_bancaria = models.ForeignKey(ContaBancaria, on_delete=models.RESTRICT, related_name='transacoes', null=True, blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.RESTRICT, related_name='transacoes')
    cartao = models.ForeignKey(CartaoDeCredito, on_delete=models.SET_NULL, related_name='transacoes', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Transações"
        ordering = ['-data']

    def __str__(self):
        return f"{self.data.strftime('%d/%m/%Y')} - {self.descricao}: R$ {self.valor}"