from django.conf.urls import url
from django.urls import path
from . import views



urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('tienda/', views.welcome, name='welcome'),
    path('tienda/listado/', views.listado, name='listado'),
    path('tienda/insertar/', views.insertar, name='insertar'),
    path('tienda/editar/<int:id>', views.editar, name='editar'),
    path('tienda/eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('tienda/compra/', views.compra, name='compra'),
    path('tienda/insertarCompra/<int:id>', views.insertarCompra, name='insertarCompra'),
]
