import pytest

from tests.factories import ItemFactory, OrderFactory


@pytest.mark.django_db
def test_ex4_list_v2_paid_orders_db_queries(client, django_assert_num_queries):
    for i in range(0,100):
        items = ItemFactory.create_batch(10)
        orders = OrderFactory.create(items=items, paid=(i % 10 == 0))

    # Three queries
    # COUNT
    # SELECT orders
    # SELECT items (prefetch)
    with django_assert_num_queries(3):
        response = client.get('/api/v2/billing/orders/paid/')

    assert response.status_code == 200
    assert response.json()['count'] == 10
