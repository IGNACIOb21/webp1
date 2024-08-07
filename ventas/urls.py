from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bienvenida/', views.bienvenida, name='bienvenida'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('olvide_contra/', views.olvide_contra, name='olvide_contra'),
    path('cambiarclave/', views.cambiarclave, name='cambiarclave'),
    path('cuenta/', views.cuenta, name='cuenta'),
    path('eliminarcuenta/', views.eliminarcuenta, name='eliminarcuenta'),

    path('ofertas/', views.ofertas, name='ofertas'),
    path('registrarse/', views.registrarse, name='registrarse'),

    path('crear_producto/', views.crear_producto, name='crear_producto'),
    path('ventana_gato/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),

    path('ventana_gato/', views.ventana_gato, name='ventana_gato'),
    path('ventana_recien_llegados/', views.recien_llegados, name='ventana_recien_llegados'),
    path('ventana_perros/', views.ventas_perros, name='ventana_perros'),


    path('ventaGato1/', views.ventaGato1, name='ventaGato1'),
    path('ventaGato2/', views.ventaGato2, name='ventaGato2'),
    path('ventaGato3/', views.ventaGato3, name='ventaGato3'),
    path('ventaGato4/', views.ventaGato4, name='ventaGato4'),
    path('ventaGato5/', views.ventaGato5, name='ventaGato5'),
    path('ventaGato6/', views.ventaGato6, name='ventaGato6'),
    path('ventaGato7/', views.ventaGato7, name='ventaGato7'),
    path('ventaGato8/', views.ventaGato8, name='ventaGato8'),
    path('ventaGato9/', views.ventaGato9, name='ventaGato9'),
    path('ventaGato10/', views.ventaGato10, name='ventaGato10'),
    path('ventaGato11/', views.ventaGato11, name='ventaGato11'),
    path('ventaGato12/', views.ventaGato12, name='ventaGato12'),
    path('ventaGato13/', views.ventaGato13, name='ventaGato13'),
    path('ventaGato14/', views.ventaGato14, name='ventaGato14'),
    path('ventaGato15/', views.ventaGato15, name='ventaGato15'),  
    path('ventaGato16/', views.ventaGato16, name='ventaGato16'),
    path('ventaGato17/', views.ventaGato17, name='ventaGato17'),
    path('ventaGato18/', views.ventaGato18, name='ventaGato18'),
    path('ventaGato19/', views.ventaGato19, name='ventaGato19'),
    path('ventaGato20/', views.ventaGato20, name='ventaGato20'),
    path('ventaGato21/', views.ventaGato21, name='ventaGato21'),
    path('ventaGato22/', views.ventaGato22, name='ventaGato22'),
    path('ventaGato23/', views.ventaGato23, name='ventaGato23'),


    path('ventas_perro1/', views.ventas_perro1, name='ventas_perro1'),
    path('ventas_perro2/', views.ventas_perro2, name='ventas_perro2'),
    path('ventas_perro3/', views.ventas_perro3, name='ventas_perro3'),
    path('ventas_perro4/', views.ventas_perro4, name='ventas_perro4'),
    path('ventas_perro5/', views.ventas_perro5, name='ventas_perro5'),
    path('ventas_perro6/', views.ventas_perro6, name='ventas_perro6'),
    path('ventas_perro7/', views.ventas_perro7, name='ventas_perro7'),


    path('recien_llegados2/', views.recien_llegados2, name='recien_llegados2'),
    path('recien_llegados3/', views.recien_llegados3, name='recien_llegados3'),
    path('recien_llegados4/', views.recien_llegados4, name='recien_llegados4'),
    path('recien_llegados5/', views.recien_llegados5, name='recien_llegados5'),
    path('recien_llegados6/', views.recien_llegados6, name='recien_llegados6'),
    path('recien_llegados7/', views.recien_llegados7, name='recien_llegados7'),
    path('recien_llegados8/', views.recien_llegados8, name='recien_llegados8'),
    path('recien_llegados9/', views.recien_llegados9, name='recien_llegados9'),
    path('recien_llegados10/', views.recien_llegados10, name='recien_llegados10'),
    path('recien_llegados11/', views.recien_llegados11, name='recien_llegados11'),
    path('recien_llegados12/', views.recien_llegados12, name='recien_llegados12'),
    path('recien_llegados13/', views.recien_llegados13, name='recien_llegados13'),
]