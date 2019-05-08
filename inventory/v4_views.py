from rest_framework import viewsets
import django_filters
from django_filters.rest_framework import FilterSet

from inventory.models import Manufacturer, Item
from inventory.v2_serializers import V2ManufacturerSerializer, V2ItemSerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all().order_by('pk')
    serializer_class = V2ManufacturerSerializer


class ItemSearchFilter(FilterSet):
    inventor = django_filters.CharFilter(field_name="inventor", method='search_by_inventor')

    class Meta:
        model = Item
        fields = ['inventor']

    def search_by_inventor(self, qs, field_name, value):
        return Item.search_by_inventor(value, qs)


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = V2ItemSerializer
    filter_class = ItemSearchFilter

    def filter_queryset(self, *args, **kwargs):
        qs = super().filter_queryset(*args, **kwargs)
        qs.select_related('manufacturer')
        return qs
