from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=128, default='', blank=True)
    country = models.CharField(max_length=128, default='', blank=True)


class Item(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, related_name='item', on_delete=models.PROTECT)
    name = models.CharField(max_length=128, default='', blank=True)
    description = models.CharField(max_length=128, default='', blank=True)
    cost = models.IntegerField()

    RED = 'RED'
    ORANGE = 'ORANGE'
    YELLOW = 'YELLOW'
    GREEN = 'GREEN'
    BLUE = 'BLUE'
    INDIGO = 'INDIGO'
    VIOLET = 'VIOLET'
    COLOR_CHOICES = (
        (RED, 'red'),
        (ORANGE, 'orange'),
        (YELLOW, 'yellow'),
        (GREEN, 'green'),
        (BLUE, 'blue'),
        (INDIGO, 'indigo'),
        (VIOLET, 'violet'),
    )
    color = models.CharField(max_length=16, choices=COLOR_CHOICES, default=RED)

    class Meta:
        indexes = (
          models.Index(fields=['description']),
        )


