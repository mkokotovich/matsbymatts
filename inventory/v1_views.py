from rest_framework import viewsets

from inventory.models import Manufacturer, Item
from inventory.v1_serializers import ManufacturerSerializer, ItemSerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all().order_by('pk')
    serializer_class = ManufacturerSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('pk')
    serializer_class = ItemSerializer
