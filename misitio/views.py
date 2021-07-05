from rest_framework import permissions
from rest_framework import serializers, viewsets
from .serializers import ProductoSerializer
from pasteleria.models import Producto





# ViewSets define the view behavior.
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    permission_classes = [permissions.IsAuthenticated]