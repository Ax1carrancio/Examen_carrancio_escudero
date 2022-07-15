from django.contrib import admin
from .models import Clientes, Productos, Categoria
# Register your models here.

admin.site.register(Clientes)
admin.site.register(Productos)
admin.site.register(Categoria)


