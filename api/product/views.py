from rest_framework import viewsets

from .models import Product
from .serializers import ProductSerializers


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializers
