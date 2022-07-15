from django.urls import path 
from unicodedata import name 
from .views import Maceta_principal, api_trabajos, contactos, galería, registro, registrar, somos, agregarCL, mostrarCL, login, form_clientes, form_eliminar_clientes, form_modclientes, MostrarPr, agregarPr, form_eliminar_productos, form_modproductos, form_productos, tienda,seguimiento

urlpatterns = [ 
    path('', Maceta_principal, name="Maceta_principal"),
    path('api_trabajos/', api_trabajos, name="api_trabajos"),
    path('contactos/', contactos, name="contactos"),
    path('galería/', galería, name="galería"), 
    path('registro/', registro, name="registro"),
    path('somos/', somos, name="somos"),
    path('agregarCL/', agregarCL, name="agregarCL"),
    path('mostrarCL/', mostrarCL, name="mostrarCL"),
    path('login/', login, name="login"),
    path('form_clientes/', form_clientes, name="form_clientes"), 
    path('form_modclientes/<id>', form_modclientes, name="form_modclientes"),
    path('form_eliminar_clientes/<id>', form_eliminar_clientes, name="form_eliminar_clientes"),
    path('MostrarPr/', MostrarPr, name = "MostrarPr" ),
    path('agregarPr/', agregarPr, name = "agregarPr"),
    path('form_eliminar_productos/<id>', form_eliminar_productos,name="form_eliminar_productos"),
    path('form_modproductos/<id>', form_modproductos, name="form_modproductos"),
    path('form_productos/', form_productos, name= "form_productos"),
    path('tienda/', tienda, name="tienda"),
    path('seguimiento/', seguimiento,name = "seguimiento"),
    #registrousuario
    path('registrar/', registrar, name="registrar"),




] 