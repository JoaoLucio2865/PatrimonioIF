from django.shortcuts import render
from . models import*

def funcao(request):
    consultas = {
        'consultas': Funcao.objects.all()
    }
    return render(request, 'consulta/Funcao.html', consultas)

def permissao(request):
    consultas = {
        'consultas':Permissao.objects.all()
    }
    return render(request, 'consulta/Permissao.html', consultas)

def colaborador(request):
    consultas = {
        'consultas':Colaborador.objects.all()
    }
    return render(request, 'consulta/Colaborador.html', consultas)

def unidade(request):
    consultas = {
        'consultas':Unidade.objects.all()
    }
    return render(request, 'consulta/Unidade.html', consultas)

def predio(request):
    consultas = {
        'consultas':Predio.objects.all()
    }
    return render(request, 'consulta/Predio.html', consultas)

def sala(request):
    consultas = {
        'consultas':Sala.objects.all()
    }
    return render(request, 'consulta/Sala.html', consultas)

def tipo(request):
    consultas = {
        'consultas':Tipo.objects.all()
    }
    return render(request, 'consulta/Tipo.html', consultas)

def patrimonio(request):
    consultas = {
        'consultas':Patrimonio.objects.all()
    }
    return render(request, 'consulta/Patrimonio.html', consultas)


def alocacao(request):
    consultas = {
        'consultas':Alocacao.objects.all()
    }
    return render(request, 'consulta/Alocacao.html', consultas)