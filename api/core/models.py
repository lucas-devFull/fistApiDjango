from django.db import models

class Endereco(models.Model):
    rua = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)

    def __str__(self):
        return self.rua

class Telefone(models.Model):
    telefone = models.IntegerField(unique=True, null=False, default=0)
    def __str__(self):
        return str(self.telefone)
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.ForeignKey(to="Endereco",on_delete=models.CASCADE)
    numeroCelular = models.ForeignKey(to="Telefone", on_delete=models.CASCADE)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome

class Teste(models.Model):
    retorno = str()
    search = ""

    def __init__(self, nome):
        self.retorno = str()
        self.search = nome
        return None

    def teste(self):
        return self.search


class FeedPost(models.Model):
    id_post = models.AutoField(primary_key=True)
    titulo_post = models.CharField(max_length=100, blank=True, null=True)
    descricao_post = models.CharField(max_length=250, blank=True, null=True)
    endereco_post = models.CharField(max_length=70, blank=True, null=True)
    data_post = models.DateField(blank=True, null=True)
    link_fb = models.CharField(max_length=250, blank=True, null=True)
    link_instagram = models.CharField(max_length=250, blank=True, null=True)
    link_twitter = models.CharField(max_length=250, blank=True, null=True)
    link_wpp = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feed_post'

class Usuario(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=30, blank=True, null=True)
    senha = models.CharField(max_length=15, blank=True, null=True)
    admin = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nome