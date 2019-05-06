import pytest

from tests.factories import ItemFactory


@pytest.mark.django_db
def test_ex2_list_v2_items_db_queries(client, django_assert_num_queries):
    ItemFactory.create_batch(10)

    # Two queries
    # COUNT
    # SELECT 
    with django_assert_num_queries(2):
        response = client.get('/api/v2/inventory/items/')

    assert response.status_code == 200
