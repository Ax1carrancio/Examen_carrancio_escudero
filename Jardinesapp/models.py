from email.mime import image
from django.db import models
from tabnanny import verbose
from email.policy import default

# Create your models here.

class Clientes(models.Model):
    rut=models.CharField(max_length=10, primary_key=True, verbose_name='Rut')
    nombre = models.CharField(max_length=10, verbose_name='Nombre')
    apellidos= models.CharField(max_length=20, verbose_name='Apellidos')
    correo=models.CharField(max_length=40, verbose_name='Correo')
    telefono= models.CharField(max_length=20, verbose_name='Telefono', default="")
    direccion=models.CharField(max_length=40, verbose_name='Direccion', default="")

    def __str__(self):
        return self.rut

class Categoria(models.Model): 
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de Categoría')
    nombreCategoria= models.CharField(max_length=50, verbose_name='Nombre de Categoría')

    def __str__(self):
        return self.nombreCategoria


class Productos(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True, verbose_name='Codigo del Producto')
    nombre_pro=models.CharField(max_length=40, verbose_name='Nombre del Producto')
    marca= models.CharField(max_length=20, verbose_name='Marca del Producto')
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.IntegerField(verbose_name='Precio', null = True)
    imagen = models.ImageField(upload_to = "productos", null = True)

    def __str__(self):
        return self.codigo



