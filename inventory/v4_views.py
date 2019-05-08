from rest_framework import viewsets
import django_filters
from django_filters.rest_framework import FilterSet

from inventory.models import Manufacturer, Item
from inventory.v2_serializers import V2ManufacturerSerializer, V2ItemSerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all().order_by('pk')
    serializer_class = V2ManufacturerSerializer


class ItemSearchFilter(FilterSet):
    name = django_filters.CharFilter(field_name="name", method='search_by_name')

    class Meta:
        model = Item
        fields = ['name']

    def search_by_name(self, qs, field_name, value):
        return Item.search_by_name(value, qs)


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = V2ItemSerializer
    filter_class = ItemSearchFilter

    def filter_queryset(self, *args, **kwargs):
        qs = super().filter_queryset(*args, **kwargs)
        qs.select_related('manufacturer')
        return qs
