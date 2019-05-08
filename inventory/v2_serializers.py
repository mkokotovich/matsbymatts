from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from inventory.models import Manufacturer, Item


class V2ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ('name', 'country')


class V2ItemSerializer(serializers.ModelSerializer):
    country_of_origin = serializers.CharField(source='manufacturer.country')

    class Meta:
        model = Item
        fields = ('manufacturer', 'name', 'description', 'color', 'cost', 'country_of_origin', 'inventor')
