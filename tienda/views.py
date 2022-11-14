from django.shortcuts import render, redirect
from .models import *
from .forms import ProductoForm, MarcaForm
from django.db.models import Q

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
    busqueda = request.GET.get("buscar")
    prd = Producto.objects.all()
    if busqueda:
        # El filter es como un where,
        # El Q, importado arriba, revisa cada campo del modelo;
        # icontains lo reconoce con mayus, minus e imcompleto
        prd = Producto.objects.filter(
            Q(nombre_P__icontains = busqueda) |
            Q(nombre_M = busqueda)
        ).distinct()

    return render(request, 'tienda/compra.html', {"prd":prd})

"""get_object_or_404, si el objeto no existe, dame este error"""
