import pytest

from tests.factories import ItemFactory, OrderFactory


@pytest.mark.django_db
def test_ex3_list_v1_orders_db_queries(client, django_assert_num_queries):
    for _ in range(0, 10):
        items = ItemFactory.create_batch(10)
        orders = OrderFactory.create(items=items)

    with django_assert_num_queries(3):
        response = client.get('/api/v1/billing/orders/')

    assert response.status_code == 200
