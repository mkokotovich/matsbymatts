from rest_framework import viewsets

from inventory.models import Manufacturer, Item
from inventory.v1_serializers import V1ManufacturerSerializer, V1ItemSerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all().order_by('pk')
    serializer_class = V1ManufacturerSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('pk')
    serializer_class = V1ItemSerializer
