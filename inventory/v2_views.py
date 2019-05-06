from rest_framework import viewsets
from rest_framework.views import APIView

from inventory.models import Manufacturer, Item
from inventory.v2_serializers import V2ManufacturerSerializer, V2ItemSerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all().order_by('pk')
    serializer_class = V2ManufacturerSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('pk')
    # queryset = Item.objects.all().order_by('pk').select_related('manufacturer')
    serializer_class = V2ItemSerializer
