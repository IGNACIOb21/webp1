from django.urls import path
from . import views

urlpatterns = [
    path('bienvenida/', views.bienvenida, name='bienvenida'),
    path('index/', views.index, name='index'),
    path('ofertas/', views.ofertas, name='ofertas'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('prueba/', views.prueba, name='prueva'),
]