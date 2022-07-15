from rest_framework import serializers
from Jardinesapp.models import Clientes


class ClientesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clientes
        fields=['nombre','apellidos', 'correo', 'rut', 'telefono', 'direccion']