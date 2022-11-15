from django.contrib import admin
from tienda.models import Producto, Marca, Vendido

# Register your models here.

#para que aparezcan los campos que le indico en el panel de administracion
class ProductoAdmin(admin.ModelAdmin):
    list_display=("nombre_P", "modelo", "unidades", "precio", "detalles", "nombre_M")

class VendidoAdmin(admin.ModelAdmin):
    list_display = ("id_compra", "id_cliente", "nombre_P", "unidades", "importe", "nombre_M")

admin.site.register(Producto)
admin.site.register(Marca)
admin.site.register(Vendido)
