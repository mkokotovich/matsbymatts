from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.SET_NULL, null=True)
    items = models.ManyToManyField('inventory.Item')
    price = models.IntegerField()
