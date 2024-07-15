from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    ventana = forms.ChoiceField(choices=(
        ('ventana_gato', 'Ventana Gato'),
        ('ventas_perros', 'Ventana Perros'),
        ('recien_llegados', 'Recién Llegados'),
    ), widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'imagen', 'ventana']



