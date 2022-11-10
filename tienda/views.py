from django.shortcuts import render
from .models import *
from .forms import ProductoForm, MarcaForm

# Create your views here.
def welcome(request):
    return render(request,'tienda/index.html', {})

def insertar(request):
    if request.method == 'POST':
        
        formulario = ProductoForm(request.POST)
        
        if formulario.is_valid():
            
            formulario.save()
            
            infForm=formulario.cleaned_data
            
            return redirect('index')
        
        else:
            
            formulario = ProductoForm()
            #va a estar vacio
            
    return render(request, 'tienda/insertar.html', {'formulario': formulario})
#Le enviamos los datos al formulario que está en insertar.html
