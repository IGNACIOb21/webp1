from django.db import models

# Create your models here.
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)  # AutoField se encarga del auto incremento
    nombre = models.CharField(max_length=20)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to="productos", null=True)
    descripcion = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre
    
class Registrar(models.Model):
    id_registrar = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True, max_length=100)
    password = models.CharField(max_length=128)  # Increased length for hashed password

    def __str__(self):
        return self.email