from rest_framework import viewsets

from billing.serializers import OrderSerializer
from billing.models import Order


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('pk')
    serializer_class = OrderSerializer
