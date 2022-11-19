from django.conf.urls import url
from django.urls import path, include
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
    path('tienda/informes/', views.informes, name='informes'),
    path('tienda/top10/', views.top10, name='top10'),
    path('tienda/porMarca/', views.porMarca, name='porMarca'),
    path('tienda/registro/', views.registro, name='registro'),
    path('tienda/cerrarSesion/', views.cerrarSesion, name='cerrarSesion'),
    path('tienda/iniciarSesion/', views.iniciarSesion, name='iniciarSesion'),
]
