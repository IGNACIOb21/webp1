from django.db import models

# Create your models here.
class Producto(models.Model):
    codigo = models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"
    
    
class Registrar(models.Model):
    id_registrar = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True, max_length=100)
    password = models.CharField(max_length=128)  # Increased length for hashed password

    def __str__(self):
        return self.email