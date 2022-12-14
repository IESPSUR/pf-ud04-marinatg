from django.shortcuts import render, redirect
from .models import *
from .forms import ProductoForm, MarcaForm, VendidoForm, UnidadesForm
from django.db.models import Q, Sum
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return render(request,'tienda/index.html', {'user':request.user})


"""CRUD"""
def listado(request):
    prd = Producto.objects.all()
    return render(request, 'tienda/listado.html', {"prd":prd})


def insertar(request):
    formulario = ProductoForm(request.POST or None)
    if request.method == 'POST':

        if formulario.is_valid():

            formulario.save()

            infForm = formulario.cleaned_data

            return redirect('listado')

        else:

            formulario = ProductoForm()
            # va a estar vacio

    return render(request, 'tienda/insertar.html', {'formulario': formulario})
    """Le enviamos los datos al formulario que está en insertar.html"""

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


"""COMPRA"""
def compra(request):
    busqueda = request.GET.get("buscar")
    prd = Producto.objects.all()

    if busqueda:
        """El filter es como un where,
        El Q, importado arriba, revisa cada campo del modelo;
        icontains lo reconoce con mayus, minus e imcompleto"""
        prd = Producto.objects.filter(
            Q(nombre_P__icontains = busqueda) |
            Q(nombre_M = busqueda)
        ).distinct()

    return render(request, 'tienda/compra.html', {"prd": prd})

def insertarCompra(request, id):
    producto = Producto.objects.get(id=id)
    marca = Marca.objects.get(nombre_M=producto.nombre_M)
    formulario = ProductoForm(request.POST or None, instance=producto)
    miformulario = UnidadesForm(request.POST)
    ventas = Vendido.objects.all()
    numVentas = len(ventas) + 1
    user = request.user

    if request.method == 'POST':
        if miformulario.is_valid():
            unidadesC = miformulario.cleaned_data['unidades']

            if producto.unidades > unidadesC:
                producto.unidades = producto.unidades - unidadesC
                producto.save()

                """MAPEO"""
                venta = Vendido(id_compra = numVentas,
                                id_cliente = user,
                                nombre_P = producto,
                                importe = unidadesC * producto.precio,
                                nombre_M = marca,
                                unidades = unidadesC)
                venta.save()
                return redirect('compra')

    return render(request, 'tienda/insertarCompra.html', {'formulario': formulario, 'unidadesForm': miformulario})


"""INFORMES"""
def informes(request):

    return render(request, 'tienda/informes.html', {})

def porMarca(request):

    marca = Producto.objects.all()
    busqueda = request.GET.get("buscar")

    busqueda = request.GET.get("buscar")
    marca = Vendido.objects.all()


    if busqueda:
        """El filter es como un where,
        El Q, importado arriba, revisa cada campo del modelo;
        icontains lo reconoce con mayus, minus e imcompleto"""

        marca = Producto.objects.filter(
            Q(nombre_M=busqueda)
        ).distinct()

        marca = Vendido.objects.filter(
            Q(nombre_M=busqueda)
        ).distinct()
    Marca.objects.filter()

    return render(request, 'tienda/porMarca.html', {'marca':marca})

def top10(request):
    """Pongo - en unidades, para orden descendente"""
    top10 = Vendido.objects.all().order_by('-unidades')[:10]

    return render(request, 'tienda/top10.html', {'top10': top10})

def porCliente(request):
    busqueda = request.GET.get("buscar")
    cliente = Vendido.objects.all()

    if busqueda:
        """El filter es como un where,"""
        """El Q, importado arriba, revisa cada campo del modelo;"""
        usuario = User.objects.filter(
            Q(username = busqueda)
        ).distinct()

        """Devuelve un array, asi que debo poner la posicion que quiero obtener"""
        cliente = Vendido.objects.filter(
            Q(id_cliente=usuario[0])
        ).distinct()

    return render(request, 'tienda/porCliente.html', {'cliente': cliente})

def top10Clientes(request):
    """Pongo - en unidades, para orden descendente
    [:X] Registros que quiero obtener --> order_by('-importe')[:10]"""

    # Partir de la tabla user. LA uno con annotate a la tabla vendido(seleccionando el campo que
    # necesito --> importe, y creando la variable suma, sumo los importes con sum), y ordeno por suma
    cliente = User.objects.annotate(suma = Sum('vendido__importe')).order_by('-suma')[:10]

    # top10C = Vendido.objects.all().values('id_cliente').annotate(suma = Sum('importe'))

    print(cliente.values())

    return render(request, 'tienda/top10Clientes.html', { 'cliente':cliente})

    cliente = User.objects.all()
    top10C = Vendido.objects.all().values('id_cliente_id').annotate(suma = Sum('importe'))

    print(top10C)
    return render(request, 'tienda/top10Clientes.html', {'top10C': top10C, 'cliente':cliente})



"""REGISTRO, LOGIN Y LOGOUT"""
def registro(request):
    if request.method == 'GET':
        return render(request, "tienda/registro.html", {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('welcome')
            except:
                return render(request, "tienda/registro.html", {'form': UserCreationForm, 'error': 'El usuario ya existe'})
        return render(request, "tienda/registro.html", {'form': UserCreationForm, 'error': 'Las contraseñas no coinciden'})

def cerrarSesion(request):
    logout(request)
    return redirect('welcome')

def iniciarSesion(request):
    if request.method == 'GET':
        return render(request, 'tienda/iniciarSesion.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'tienda/iniciarSesion.html', {'form': AuthenticationForm, 'error': 'El usuario o la contraseña son incorrectos'})
        else:
            login(request, user)
            return redirect('welcome')
