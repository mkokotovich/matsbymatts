import random
from itertools import chain
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import django
django.setup()

from tests.factories import UserFactory, ManufacturerFactory, ItemFactory, OrderFactory


def main(num_manufacturers, num_items_per_man, num_orders):
    mans = ManufacturerFactory.create_batch(num_manufacturers)
    print(f"Created {num_manufacturers} Manufacturers")

    items = list(chain.from_iterable([ItemFactory.create_batch(num_items_per_man, manufacturer=man) for man in mans]))
    print(f"Created {len(items)} Items")

    users = UserFactory.create_batch(50)
    for _ in range(0, num_orders):
        num_items = random.randint(5,20)
        user = random.choice(users)
        OrderFactory.create(user=user, items=random.sample(items, num_items))
    print(f"Created {num_orders} Orders")


if __name__ == '__main__':

    num_manufacturers = 250
    num_items_per_man = 200
    num_orders = 50

    main(num_manufacturers, num_items_per_man, num_orders)
