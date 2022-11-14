from django.db import models

# Create your models here.
class Marca(models.Model):
    #Si no quiero poner primary key --> unique
    nombre_M = models.CharField(max_length=30, primary_key=True)
    
    #para que en el panel de administracion salga el nombre y no Producto object..
    def __str__(self):
        return self.nombre_M
    
class Producto(models.Model):
    id = models.IntegerField("Id", primary_key=True)
    nombre_P = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    unidades = models.IntegerField("Unidades")
    precio = models.FloatField("Precio")
    detalles = models.CharField(max_length=30)
    """Protect no te deja borrar, rerstrict solo si borras todo el arbol de dependencias"""
    nombre_M = models.ForeignKey(Marca, models.PROTECT)

    def __str__(self):
        return self.nombre_P

class Vendido(models.Model):
    id_compra = models.IntegerField("Id_Compra", primary_key=True)
    id_cliente = models.IntegerField("Id_Cliente")
    nombre_P = models.CharField(max_length=30)
    unidades = models.IntegerField("Unidades")
    importe = models.FloatField("Importe")
    nombre_M = models.CharField(max_length=30)

    """Poner e campo usuariodel tipo setings.AUTH_USER..
    poner un campo fecha"""


