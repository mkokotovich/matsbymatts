from rest_framework import viewsets

from billing.v1_serializers import V1OrderSerializer
from billing.models import Order


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('pk')
    queryset = Order.objects.all().order_by('pk').prefetch_related('items')
    serializer_class = V1OrderSerializer
