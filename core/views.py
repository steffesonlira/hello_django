from django.shortcuts import render, HttpResponse


# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(nome, idade))


def soma(request, a, b, soma):
    soma = a + b
    return HttpResponse('<h2>A soma entre {} e {} é: {som}'.format(a,b,som=soma))
