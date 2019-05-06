from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from billing.models import Order


class V1OrderSerializer(serializers.ModelSerializer):
    total_cost = SerializerMethodField()

    def get_total_cost(self, obj):
        return sum(item.cost for item in obj.items.all())

    class Meta:
        model = Order
        fields = ('user', 'items', 'total_cost', 'paid')
