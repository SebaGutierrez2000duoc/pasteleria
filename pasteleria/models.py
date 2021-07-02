from django.db import models

# Create your models here.
class Producto(models.Model):
	producto = models.CharField(max_length=30)
	precio = models.IntegerField(default=0)
	mensaje = models.CharField(max_length=30)
	sabor = models.CharField(max_length=20)
	cantidad = models.IntegerField(default=0)

	def __str__(self):
		return self.producto
