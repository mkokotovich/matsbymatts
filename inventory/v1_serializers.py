from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from inventory.models import Manufacturer, Item


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ('name', 'country')


class ItemSerializer(serializers.ModelSerializer):
    manufacturer_display = SerializerMethodField('get_manufacturer')

    def get_manufacturer(self, obj):
        return f"Manufacturer ID: {obj.manufacturer.id}"

    class Meta:
        model = Item
        fields = ('manufacturer_display', 'part_number', 'description', 'cost')
