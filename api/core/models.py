from django.db import models

class Endereco(models.Model):
    rua = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)

    def __str__(self):
        return self.rua
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.ForeignKey(Endereco, related_name='endereco',  on_delete=models.CASCADE)
    # endereco = models.CharField(max_length=50)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome

