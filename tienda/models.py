from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre_M = models.CharField(max_length=30, primary_key=True)
    
    #para que en el panel de administracion salga el nombre y no Producto object..
    def __str__(self):
        return self.nombre_M
    
class Producto(models.Model):
    nombre_P = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    unidades = models.IntegerField
    precio = models.IntegerField
    detalles = models.CharField(max_length=30)
    nombre_M = models.ForeignKey(Marca, on_delete=models.CASCADE)


