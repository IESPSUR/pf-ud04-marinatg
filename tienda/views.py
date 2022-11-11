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
    formulario = ProductoForm(request.POST)
    if request.method == 'POST':
        
        if formulario.is_valid():
            
            formulario.save()
            
            infForm=formulario.cleaned_data
            
            return redirect('tienda/insertar/')
        
        else:
            
            formulario = ProductoForm()
            #va a estar vacio
            
    return render(request, 'tienda/insertar.html', {'formulario': formulario})
#Le enviamos los datos al formulario que está en insertar.html
