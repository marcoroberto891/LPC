from django.db import models

class Pessoa(models.Model):
    nome = models.CharField('nome',max_length=50)
    descricao = models.TextField()
    data_nascimento = models.DateTimeField(blank= True,null=True)
    telefone = models.CharField(max_length=12,blank= True,null=True)

    def __str__(self):
        return  self.nome

# Create your models here.
