from django.db import models

class Funcao(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome

class Permissao(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome

class Colaborador(models.Model):
    nome = models.CharField(max_length=50)
    funcao = models.ForeignKey(Funcao, on_delete=models.CASCADE)
    permissao = models.ForeignKey(Permissao, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.nome} - {self.funcao} - {self.permissao}'
    
class Unidade(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    cep = models.CharField(max_length=10)
    def __str__(self):
        return f'{self.nome} - {self.endereco} - {self.numero}  - {self.bairro} - {self.cidade} - {self.cep}'
    
class Predio(models.Model):
    nome = models.CharField(max_length=50)   
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.nome} - {self.unidade}'
    
class Sala(models.Model):
    nome = models.CharField(max_length=50)   
    predio = models.ForeignKey(Predio, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.nome} - {self.predio}'
    
class Tipo(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome
    
class Patrimonio(models.Model):
    matricula = models.CharField(max_length=50)   
    nome = models.CharField(max_length=50)   
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.matricula} - {self.nome} - {self.tipo}'
    
class Alocacao(models.Model):
    patrimonio = models.ForeignKey(Patrimonio, on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.patrimonio} - {self.sala}'