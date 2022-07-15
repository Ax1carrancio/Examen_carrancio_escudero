from django.shortcuts import render, redirect
from django.views.decorators import csrf
from .models import Clientes, Productos
from .forms import ClientesForm, ProductosForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def Maceta_principal(request):

    return render(request, 'Maceta_principal.html')

def contactos(request):

    return render(request, 'contactos.html')

def galería(request):

    return render(request, 'galería.html')

def api_trabajos(request):

    return render(request, 'api_trabajos.html')

def registro(request):

    return render(request, 'registro.html') 

def somos(request):

    return render(request,'somos.html')

def agregarCL(request):

    return render(request,'agregarCL.html')


def login(request):

    return render(request,'login.html')

def agregarPr(request):

    return render(request, 'agregarPr.html')





def mostrarCL(request):
    clientes = Clientes.objects.all()
    datos = {
        'clientes' : clientes
    }
    return render(request, 'mostrarCL.html', datos)

def form_clientes(request): 

    if request.method=='POST':
        clientes_form = ClientesForm(request.POST)
        if clientes_form.is_valid():
            clientes_form.save()
            return redirect ('mostrarCL')
    else:
        clientes_form = ClientesForm()
    return render(request, 'agregarCL.html', {'clientes_form': clientes_form})


def form_modclientes(request, id):
    clientes = Clientes.objects.get(rut=id)
    datos = {
        'form': ClientesForm(instance = clientes)
    }
    if request.method=='POST':
        formulario = ClientesForm(data=request.POST, instance = clientes)
        if formulario.is_valid():
            formulario.save()
            return redirect ('mostrarCL')
        
    return render(request, 'form_modclientes.html', datos)


def form_eliminar_clientes(request,id):
    clientes = Clientes.objects.get(rut=id)
    clientes.delete()
    return redirect('mostrarCL')



def MostrarPr(request):
    productos = Productos.objects.all()
    datos = {
        'productos' : productos
    }
    return render(request, 'MostrarPr.html', datos)

def form_productos(request): 

    if request.method=='POST':
        productos_form = ProductosForm(request.POST)
        if productos_form.is_valid():
            productos_form.save()
            return redirect ('MostrarPr')
    else:
        productos_form = ProductosForm()
    return render(request, 'agregarPr.html', {'productos_form': productos_form})

def form_modproductos(request, id):
    productos = Productos.objects.get(codigo=id)
    datos = {
        'form': ProductosForm(instance = productos)
    }
    if request.method=='POST':
        formulario = ProductosForm(data=request.POST, instance = productos)
        if formulario.is_valid():
            formulario.save()
            return redirect ('MostrarPr')
        
    return render(request, 'form_modproductos.html', datos)

def form_eliminar_productos(request,id):
    productos = Productos.objects.get(codigo=id)
    productos.delete()
    return redirect('MostrarPr')

#Carrito

def tienda(request):

    return render(request, 'tienda.html')

#formregistro

def registrar(request):
    data = {
        'form': CustomUserCreationForm()

    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user =  authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="Maceta_principal")
        data["form"] = formulario


    return render(request, 'registration/registrar.html', data)

#seguimiento
def seguimiento(request):
    productos = Productos.objects.all()
    datos = {
        'productos' : productos
    }
    return render(request, 'seguimiento.html', datos)
