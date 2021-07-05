from rest_framework import routers, serializers, viewsets
from pasteleria.models import Producto


# Serializers define the API representation.
class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ['url','producto', 'precio', 'descripcion']



