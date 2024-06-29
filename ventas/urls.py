from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bienvenida/', views.bienvenida, name='bienvenida'),
    path('ofertas/', views.ofertas, name='ofertas'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('prueba/', views.prueba, name='prueva'),

    path('ventana_gato/', views.ventana_gato, name='ventana_gato'),
    path('ventana_recien_llegados/', views.ventana_recien_llegados, name='ventana_recien_llegados'),
    path('ventana_recien_llegados/', views.ventana_recien_llegados, name='ventana_recien_llegados'),


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

]