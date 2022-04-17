from django.db import models
from django.contrib.auth.models import AbstractUser

"""
Criação de classe usuário genérica com flag para os tipos específicos de usuários
"""
class User(AbstractUser):
    is_produtor = models.BooleanField(default=False)
    is_consumidor = models.BooleanField(default=False)

"""
Classe de usuário que fornece os produtos
"""
class Produtor(models.Model):
    usuario = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    whatsapp = models.CharField(max_length=15, null=True)
    endereco = models.CharField(max_length=200, null=True)
    cpf = models.CharField(max_length=11, null=True)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    produtor = models.ForeignKey(Produtor, on_delete=models.CASCADE, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=40)
    valor = models.FloatField()
    MEDIDA_CHOICE = (
        ('gm', 'grama'),
        ('kg', 'quilo'),
        ('l', 'litro'),
        ('u', 'unidade'),
        ('dz', 'dúzia'),
    )
    medida = models.CharField(max_length=2, choices=MEDIDA_CHOICE)
    organico = models.BooleanField(default=False, blank=True, null=True)
    descricao= models.TextField(max_length=500)
    imagem = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.nome

    @property
    def ImagemURL(self):
        try:
            url = self.imagem.url
        except:
            url = ''
        return url

"""
Classe de usuários que trocam (consumem) os produtos ofertados
"""

class Consumidor(models.Model):
    usuario = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    whatsapp = models.CharField(max_length=15, null=True)
    cpf = models.CharField(max_length=11, null=True)

    def __str__(self):
        return self.nome

class Lista(models.Model):
    consumidor = models.ForeignKey(Consumidor, on_delete=models.CASCADE, blank=True, null=True)
    data_pedido = models.DateTimeField(auto_now_add=True)
    id_pedido = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_total_lista(self):
        itemlistas = self.itemlista_set.all()
        total = sum([item.obter_total for item in itemlistas])
        return total

    @property
    def get_total_items(self):
        itemlistas = self.itemlista_set.all()
        total = sum([item.quantidade for item in itemlistas])
        return total

class ItemLista(models.Model):
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE, blank=True, null=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, blank=True, null=True)
    quantidade = models.IntegerField(default=0, null=True, blank=True)
    data_adicao = models.DateTimeField(auto_now_add=True)

    @property
    def obter_total(self):
        total = self.produto.valor * self.quantidade
        return total

