from django.db import models
from django.urls import reverse
import uuid

# Create your models here.


class Producto(models.Model):

    codigo_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    valor = models.IntegerField()

    def get_absolute_url(self):
        return reverse('producto-detail', args=[str(self.codigo_producto)])


class Contacto(models.Model):

    identificador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.IntegerField()
    fecha = models.DateField()
    motivo = models.CharField(max_length=10)
    comentario = models.CharField(max_length=2000)

    def get_absolute_url(self):
        return reverse('contacto-detail', args=[str(self.identificador)])


class Pedido(models.Model):

    numero_pedido = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.IntegerField()
    fecha = models.DateField()
    descripcion = models.CharField(max_length=1000)
    valor = models.IntegerField()
    estado = models.CharField(max_length=10)

    def get_absolute_url(self):
        return reverse('pedido-detail', args=[str(self.numero_pedido)])
