from rest_framework import viewsets
from rest_framework.decorators import action

from billing.v1_serializers import V1OrderSerializer
from billing.models import Order


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('pk').prefetch_related('items')
    serializer_class = V1OrderSerializer

    @action(detail=False, methods=['get'])
    def paid(self, request):
        paid_orders = self.get_queryset().filter(paid=True)
        page = self.paginate_queryset(paid_orders)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(paid_orders, many=True)
        return Response(serializer.data)
