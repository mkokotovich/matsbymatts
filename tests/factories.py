import random

import factory
from coolname import generate

from inventory.models import Manufacturer, Item
from billing.models import Order


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'auth.User'
    username = factory.Faker("email")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")


class ManufacturerFactory(factory.DjangoModelFactory):
    class Meta:
        model = Manufacturer

    name = factory.LazyFunction(lambda: ' '.join(generate(2)))
    country = factory.Faker('country')


class ItemFactory(factory.DjangoModelFactory):
    class Meta:
        model = Item

    name = factory.LazyFunction(lambda: ' '.join(generate()))
    description = factory.LazyFunction(lambda: ' '.join(generate()))
    cost = factory.LazyFunction(lambda: random.randint(10, 10000))
    color = factory.LazyFunction(lambda: random.choice(('RED', 'ORANGE', 'YELLOW', 'GREEN', 'BLUE', 'INDIGO', 'VIOLET')))
    manufacturer = factory.SubFactory(ManufacturerFactory)


class OrderFactory(factory.DjangoModelFactory):
    class Meta:
        model = Order

    user = factory.SubFactory(UserFactory)

    @factory.post_generation
    def items(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of services were passed in, use them
            for item in extracted:
                self.items.add(item)
