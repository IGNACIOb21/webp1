from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductoForm  
from .models import Producto
# Inicio

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('crear_producto')
    else:
        form = ProductoForm()
    return render(request, 'ventanas/crear_producto.html', {'form': form})

def ventana_gato(request):
    productos = Producto.objects.all()
    return render(request, 'ventanas/ventana_gato.html', {'productos': productos})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'gatos/detalle_producto.html', {'producto': producto})


def index(request):
    context = {}
    return render(request, 'inicio/index.html', context)

def bienvenida(request):
    context = {}
    return render(request, 'inicio/bienvenida.html', context)

def registrarse(request):
    context = {}
    return render(request, 'inicio/registrarse.html', context)

# Ventanas
def ofertas(request):
    context = {}
    return render(request, 'ventanas/ofertas.html', context)

def ventana_recien_llegados(request):
    context = {}
    return render(request, 'ventanas/ventana_recien_llegados.html', context)

def ventas_perros(request):
    context = {}
    return render(request, 'ventanas/ventas_perros.html', context)


#Ventanas de productos Perros

def ventas_perro1(request):
    context = {}
    return render(request, 'perros/ventas_perro1.html', context)

def ventas_perro2(request):
    context = {}
    return render(request, 'perros/ventas_perro2.html', context)

def ventas_perro3(request):
    context = {}
    return render(request, 'perros/ventas_perro3.html', context)

def ventas_perro4(request):
    context = {}
    return render(request, 'perros/ventas_perro4.html', context)

def ventas_perro5(request):
    context = {}
    return render(request, 'perros/ventas_perro5.html', context)

def ventas_perro6(request):
    context = {}
    return render(request, 'perros/ventas_perro6.html', context)

def ventas_perro7(request):
    context = {}
    return render(request, 'perros/ventas_perro7.html', context)

#Ventanas de productos gatos

def ventaGato1(request):
    context = {}
    return render(request, 'gatos/ventaGato1.html', context)
def ventaGato2(request):
    context = {}
    return render(request, 'gatos/ventaGato2.html', context)
def ventaGato3(request):
    context = {}
    return render(request, 'gatos/ventaGato3.html', context)
def ventaGato4(request):
    context = {}
    return render(request, 'gatos/ventaGato4.html', context)
def ventaGato5(request):
    context = {}
    return render(request, 'gatos/ventaGato5.html', context)
def ventaGato6(request):
    context = {}
    return render(request, 'gatos/ventaGato6.html', context)
def ventaGato7(request):
    context = {}
    return render(request, 'gatos/ventaGato7.html', context)
def ventaGato8(request):
    context = {}
    return render(request, 'gatos/ventaGato8.html', context)
def ventaGato9(request):
    context = {}
    return render(request, 'gatos/ventaGato9.html', context)
def ventaGato10(request):
    context = {}
    return render(request, 'gatos/ventaGato10.html', context)
def ventaGato11(request):
    context = {}
    return render(request, 'gatos/ventaGato11.html', context)
def ventaGato12(request):
    context = {}
    return render(request, 'gatos/ventaGato12.html', context)
def ventaGato13(request):
    context = {}
    return render(request, 'gatos/ventaGato13.html', context)
def ventaGato14(request):
    context = {}
    return render(request, 'gatos/ventaGato14.html', context)
def ventaGato15(request):
    context = {}
    return render(request, 'gatos/ventaGato15.html', context)
def ventaGato16(request):
    context = {}
    return render(request, 'gatos/ventaGato16.html', context)
def ventaGato17(request):
    context = {}
    return render(request, 'gatos/ventaGato17.html', context)
def ventaGato18(request):
    context = {}
    return render(request, 'gatos/ventaGato18.html', context)
def ventaGato19(request):
    context = {}
    return render(request, 'gatos/ventaGato19.html', context)
def ventaGato20(request):
    context = {}
    return render(request, 'gatos/ventaGato20.html', context)
def ventaGato21(request):
    context = {}
    return render(request, 'gatos/ventaGato21.html', context)
def ventaGato22(request):
    context = {}
    return render(request, 'gatos/ventaGato22.html', context)
def ventaGato23(request):
    context = {}
    return render(request, 'gatos/ventaGato23.html', context)

#Ventanas de productos recien llegados

def recien_llegados2(request):
    context = {}
    return render(request, 'recien_llegados/recien_llegados2.html', context)

def recien_llegados3(request):
    context = {}
    return render(request, 'recien_llegados/recien_llegados3.html', context)

def recien_llegados4(request):
    context = {}
    return render(request, 'recien_llegados/recien_llegados4.html', context)

def recien_llegados5(request):
    context = {}
    return render(request, 'recien_llegados/recien_llegados5.html', context)

def recien_llegados6(request):
    context = {}
    return render(request, 'recien_llegados/recien_llegados6.html', context)

def recien_llegados7(request):
    context = {}
    return render(request, 'recien_llegados/recien_llegados7.html', context)

def recien_llegados8(request):
    context = {}
    return render(request, 'recien_llegados/recien_llegados8.html', context)

def recien_llegados9(request):
    context = {}
    return render(request, 'recien_llegados/recien_llegados9.html', context)

def recien_llegados10(request):
    context = {}
    return render(request, 'recien_llegados/recien_llegados10.html', context)

def recien_llegados11(request):
    context = {}
    return render(request, 'recien_llegados/recien_llegados11.html', context)

def recien_llegados12(request):
    context = {}
    return render(request, 'recien_llegados/recien_llegados12.html', context)

def recien_llegados13(request):
    context = {}
    return render(request, 'recien_llegados/recien_llegados13.html', context)
