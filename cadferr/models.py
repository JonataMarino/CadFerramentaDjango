from django.db import models

# Create your models here.
class Ferramenta(models.Model):
    codigo = models.CharField(max_length=8)
    descrição = models.CharField(max_length=10)
    tipo = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    duração = models.CharField(max_length=50)
    dataCadastro = models.CharField(max_length=10)
    função = models.CharField(max_length=100)

    def __str__(self):
        return self.nome