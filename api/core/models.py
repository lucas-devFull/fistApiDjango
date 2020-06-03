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

