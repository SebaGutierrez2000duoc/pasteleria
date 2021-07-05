from django.db import models
from django.db.models.base import Model

# Create your models here.
class Cliente(models.Model):
	rut = models.CharField(max_length=30)
	nombre = models.CharField(max_length=30)
	apellidoP = models.CharField(max_length=30)
	apellidoM = models.CharField(max_length=30)
	direccion = models.CharField(max_length=50)
	correo = models.CharField(max_length=40)
	contraseña = models.CharField(max_length=80)

	def __str__(self):
		return self.rut
		
class Producto(models.Model):
	producto = models.CharField(max_length=30)
	precio = models.IntegerField(default=0)
	descripcion = models.CharField(max_length=30)
	sabor = models.CharField(max_length=20)
	cantidad = models.IntegerField(default=0)

	def __str__(self):
		return self.producto





