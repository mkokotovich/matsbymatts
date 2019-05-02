from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=128, default='', blank=True)
    country = models.CharField(max_length=128, default='', blank=True)


class Item(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, related_name='item', on_delete=models.PROTECT)
    part_number = models.CharField(max_length=64, default='', blank=True)
    description = models.CharField(max_length=128, default='', blank=True)
    cost = models.IntegerField()
