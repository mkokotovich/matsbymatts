import random

import factory
from coolname import generate

from inventory.models import Manufacturer, Item


class ManufacturerFactory(factory.DjangoModelFactory):
    class Meta:
        model = Manufacturer

    name = ' '.join(generate(2))
    country = factory.Faker('country')


class ItemFactory(factory.DjangoModelFactory):
    class Meta:
        model = Item

    name = ' '.join(generate())
    cost = random.randint(10, 10000)
    color = random.choice(('RED', 'ORANGE', 'YELLOW', 'GREEN', 'BLUE', 'INDIGO', 'VIOLET'))
    manufacturer = factory.SubFactory(ManufacturerFactory)
