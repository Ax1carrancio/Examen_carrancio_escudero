from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Clientes, Productos, Categoria
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ClientesForm(forms.ModelForm):

    class Meta: 
        model= Clientes
        fields = ['nombre', 'apellidos', 'correo', 'rut', 'telefono', 'direccion']
        labels ={
            'nombre': 'Nombre', 
            'apellidos': 'Apellidos', 
            'correo': 'Correo',
            'rut': 'Rut',
            'telefono': 'Telefono',
            'direccion': 'Direccion'
            
        }
        widgets={
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su nombre', 
                    'id': 'nombre'
                }
            ), 
            'apellidos': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese apellidos', 
                    'id': 'apellidos'
                }
            ), 
            'correo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su correo', 
                    'id': 'correo'
                }
            ), 
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su rut', 
                    'id': 'rut',
                }
            
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su telefono', 
                    'id': 'telefono',
                }
            
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su direccion', 
                    'id': 'direccion',
                }
            
            )

        }

class ProductosForm(forms.ModelForm):


    class Meta: 
        model= Productos
        fields = ['nombre_pro', 'codigo', 'marca', 'categoria']
        labels ={
            'nombre_pro': 'Nombre Producto', 
            'codigo': 'Codigo',
            'marca' : 'Marca',
            'categoria' : 'Categoria'

            
        }
        widgets={
            'nombre_pro': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Nombre Producto', 
                    'id': 'nombre_pro'
                }
            ), 
            'codigo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Codigo del Producto', 
                    'id': 'codigo'
                }
            ), 
            'marca': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Marca del Producto', 
                    'id': 'marca'
                }
            ), 
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria',
                }
            )

        }


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]

 

