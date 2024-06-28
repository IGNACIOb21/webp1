from django.shortcuts import render

def bienvenida(request):
    context = {}
    return render(request, 'inicio/bienvenida.html', context)

def index(request):
    context = {}
    return render(request, 'inicio/index.html', context)

def ofertas(request):
    context = {}
    return render(request, 'inicio/ofertas.html', context)

def registrarse(request):
    context = {}
    return render(request, 'inicio/registrarse.html', context)

def prueba(request):
    context = {}
    return render(request, 'inicio/prueba.html', context)
