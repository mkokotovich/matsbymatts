from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from inventory.models import Manufacturer, Item


class V1ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ('name', 'country')


class V1ItemSerializer(serializers.ModelSerializer):
    #manufacturer = SerializerMethodField()
    #def get_manufacturer(self, obj):
    #    return f"Manufacturer ID: {obj.manufacturer.id}"

    class Meta:
        model = Item
        fields = ('manufacturer', 'name', 'cost')
