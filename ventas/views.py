from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductoForm
from .models import Producto, Registrar 
from django.contrib.auth.hashers import make_password
from django.contrib import messages
# Inicio

# def crear_producto(request):
#     if request.method == 'POST':
#         form = ProductoForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('crear_producto')
#     else:
#         form = ProductoForm()
#     return render(request, 'ventanas/crear_producto.html', {'form': form})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            ventana = form.cleaned_data['ventana']
            producto = form.save(commit=False)
            producto.ventana = ventana
            producto.save()
            messages.success(request, 'Producto creado exitosamente.')
            
            # Redireccionar según la ventana seleccionada
            if ventana == 'ventana_gato':
                return redirect('ventana_gato') 
            elif ventana == 'ventana_perros':
                return redirect('ventana_perros') 
            elif ventana == 'recien_llegados':
                return redirect('ventana_recien_llegados')  
    else:
        form = ProductoForm()
    
    context = {'form': form}
    return render(request, 'ventanas/crear_producto.html', context)

def ventana_gato(request):
    productos = Producto.objects.filter(ventana='ventana_gato')
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
    if request.method == "POST":
        emailt = request.POST["email"]
        passwordr = request.POST["password"]
        con_password = request.POST["con_password"]

        if passwordr == con_password:
            form = Registrar.objects.create(email=emailt, password=passwordr)
            form.save()
            return redirect('index')  # Redirecciona después de guardar
        else:
            error_message = "Las contraseñas no coinciden"
            return render(request, 'inicio/registrarse.html', {'error_message': error_message})

    return render(request, 'inicio/registrarse.html')

def olvide_contra(request):
    if request.method == "POST":
        email_ingresado = request.POST.get("email")
        try:
            registrado = Registrar.objects.get(email=email_ingresado)
            return redirect('cambiarclave')  
        except Registrar.DoesNotExist:
            pass  
    return render(request, 'inicio/olvide_contra.html')

def cambiarclave(request):
    if request.method == 'POST':
        email_ingresado = request.POST['email']
        nueva_contraseña = request.POST['contraseña']
        repetir_contraseña = request.POST['contraseñarepit']
        if nueva_contraseña == repetir_contraseña:
            try:
                usuario = Registrar.objects.get(email=email_ingresado)
                usuario.password = make_password(nueva_contraseña)
                usuario.save()
                messages.success(request, '¡Contraseña actualizada exitosamente!')
                return redirect('index')
            except Registrar.DoesNotExist:
                messages.error(request, 'El usuario con ese email no existe.')
        else:
            messages.error(request, 'Las contraseñas no coinciden.')
    return render(request, 'inicio/cambiarclave.html')

def eliminarcuenta(request):
    if request.method == "POST":
        email = request.POST.get('email')
        try:
            usuario = Registrar.objects.get(email=email)
            usuario.delete()  
            messages.success(request, 'La cuenta ha sido eliminada exitosamente.')
            return redirect('index')  
        except Registrar.DoesNotExist:
            messages.error(request, 'El email proporcionado no existe.')
    context = {}
    return render(request, 'inicio/eliminarcuenta.html', context)

def cuenta(request):
    if request.method == "POST":
        email_ingresado = request.POST.get("email")
        try:
            registrado = Registrar.objects.get(email=email_ingresado)
            return redirect('eliminarcuenta')  
        except Registrar.DoesNotExist:
            pass  
    return render(request, 'inicio/cuenta.html')

# Ventanas
def ofertas(request):
    context = {}
    return render(request, 'ventanas/ofertas.html', context)

def recien_llegados(request):
    productos = Producto.objects.filter(ventana='recien_llegados')
    return render(request, 'ventanas/ventana_recien_llegados.html', {'productos': productos})

def ventas_perros(request):
    productos = Producto.objects.filter(ventana='ventas_perros')
    return render(request, 'ventanas/ventas_perros.html', {'productos': productos})


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
