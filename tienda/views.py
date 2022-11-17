from django.shortcuts import render, redirect
from .models import *
from .forms import ProductoForm, MarcaForm, VendidoForm, UnidadesForm
from django.db.models import Q
from django.db import transaction

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

    return render(request, 'tienda/compra.html', {"prd": prd})

def insertarCompra(request, id):
    producto = Producto.objects.get(id=id)
    marca = Marca.objects.get(nombre_M=producto.nombre_M)
    formulario = ProductoForm(request.POST or None, instance=producto)
    # formularioV = VendidoForm(request.POST or None)
    miformulario = UnidadesForm(request.POST)
    ventas = Vendido.objects.all()
    numVentas = len(ventas) + 1

    if request.method == 'POST':
        if miformulario.is_valid():
            unidadesC = miformulario.cleaned_data['unidades']

            if producto.unidades > unidadesC:
                producto.unidades = producto.unidades - unidadesC
                producto.save()

                venta = Vendido(id_compra = numVentas,
                                id_cliente = 1,
                                nombre_P = producto,
                                importe = unidadesC * producto.precio,
                                nombre_M = marca,
                                unidades = unidadesC)
                venta.save()

            # if formularioV.is_valid():
            #     formularioV.save()

    return render(request, 'tienda/insertarCompra.html', {'formulario': formulario, 'unidadesForm': miformulario})

def informes(request):

    return render(request, 'tienda/informes.html', {})

def porMarca(request):
    busqueda = request.GET.get("buscar")
    marca = Vendido.objects.all()

    if busqueda:
        marca = Vendido.objects.filter(
            Q(nombre_M=busqueda)
        ).distinct()
    return render(request, 'tienda/porMarca.html', {'marca': marca})

def top10(request):
    # Pongo - en unidades, para orden descendente
    top10 = Vendido.objects.all().order_by('-unidades')[:10]

    return render(request, 'tienda/top10.html', {'top10': top10})