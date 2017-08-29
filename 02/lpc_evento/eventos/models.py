from django.db import models
from django.contrib.auth.models import User

class Endereco(models.Model):
    logradouro = models.CharField(max_length=128)
    complemento = models.CharField(max_length=256)
    uf = models.CharField(max_length=2,null=True)
    cidade = models.CharField(max_length=64,null=True)
    cep = models.CharField(max_length=10)

    def __str__(self):
        return '{} - {}, {}'.format(self.logradouro,self.cidade,self.cidade,self.uf)

class Pessoa(models.Model):
    #cpf = models.CharField(max_length=128)
    nome = models.CharField(max_length=128)
    descricao = models.TextField()
    data_nascimento = models.DateField(blank=True, null=True)
    endereco = models.ForeignKey(Endereco, related_name='pessoas',null=True,blank=False)
    usuario = models.OneToOneField(User)

    def __str__(self):
        return self.nome


class PessoaFisica(Pessoa):
    cpf = models.CharField(max_length=128)
    mae = models.CharField(max_length=128)
    pai = models.CharField(max_length=128)


class Evento(models.Model):
    realizador = models.ForeignKey(PessoaFisica,null=True,blank=False)
    endereco = models.ForeignKey(Endereco,null=True)

class Inscricao(models.Model):
    evento = models.ForeignKey(Evento)
    pessoa = models.ForeignKey(PessoaFisica)
    data = models.DateTimeField()
    preco = models.FloatField()

