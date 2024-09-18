from rest_framework import viewsets
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductSerializer
from .filters import ProductFilter
from django.core.cache import cache
from rest_framework.response import Response


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = ProductFilter
    ordering_fields = '__all__'
    ordering = ['id']
    
    
    def retrieve(self, request, *args, **kwargs):
        cache_key = f'product_{kwargs["pk"]}'
        product = cache.get(cache_key)

        if not product:
            product = self.get_object()
            cache.set(cache_key, product, timeout=60 * 15)  

        serializer = self.get_serializer(product)
        return Response(serializer.data)








