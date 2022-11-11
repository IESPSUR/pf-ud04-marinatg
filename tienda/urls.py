from django.conf.urls import url
from django.urls import path
from . import views



urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('tienda/', views.welcome, name='welcome'),
    path('tienda/insertar/', views.insertar, name='insertar'),
    path('tienda/listado/', views.listado, name='listado'),
]
