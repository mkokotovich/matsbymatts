from rest_framework import viewsets
import django_filters
from django_filters.rest_framework import FilterSet

from inventory.models import Manufacturer, Item
from inventory.v2_serializers import V2ManufacturerSerializer, V2ItemSerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all().order_by('pk')
    serializer_class = V2ManufacturerSerializer


class ItemFilter(FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr='icontains')
    description = django_filters.CharFilter(field_name="description", lookup_expr='icontains')
    color = django_filters.CharFilter(field_name="color", lookup_expr='istartswith')
    country = django_filters.CharFilter(field_name="manufacturer__country", lookup_expr='istartswith')


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('pk').select_related('manufacturer')
    serializer_class = V2ItemSerializer
    filter_class = ItemFilter
