# filters.py
import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    price_lte = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['price_lte']

