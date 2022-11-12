from django.shortcuts import render, redirect
from .models import *
from .forms import ProductoForm, MarcaForm

# Create your views here.
def welcome(request):
    return render(request,'tienda/index.html', {})

def listado(request):
    prd = Producto.objects.all()
    return render(request, 'tienda/listado.html', {"prd":prd})

def insertar(request):
    formulario = ProductoForm(request.POST or None)
    if request.method == 'POST':
        
        if formulario.is_valid():
            
            formulario.save()
            
            infForm=formulario.cleaned_data
            
            return redirect('listado')
        
        else:
            
            formulario = ProductoForm()
            #va a estar vacio
            
    return render(request, 'tienda/insertar.html', {'formulario': formulario})
#Le enviamos los datos al formulario que está en insertar.html

def editar(request, id):
    producto = Producto.objects.get(id=id)
    formulario = ProductoForm(request.POST or None, instance=producto)
    if request.method == 'POST':

        if formulario.is_valid():

            formulario.save()

            infForm = formulario.cleaned_data

            return redirect('listado')

        else:

            formulario = ProductoForm()
    return render(request,'tienda/editar.html', {'formulario':formulario})

def eliminar(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('listado')

def compra(request):
    prd = Producto.objects.all()
    return render(request, 'tienda/compra.html', {"prd":prd})

def buscar(request, nombre_P):
    prd = Producto.objects.get(nombre_P = nombre_P)
    formulario = ProductoForm(request.GET or None, instance=prd)
    if request.method == 'GET':

        if formulario.is_valid():

            formulario.save()

            infForm = formulario.cleaned_data

            return redirect('tienda/buscado.html')

        else:

            formulario = ProductoForm()

    return render(request, 'tienda/compra.html', {"prd": prd})