import pytest
from django.test.utils import CaptureQueriesContext
from django.db import connection

from tests.factories import ItemFactory

@pytest.mark.django_db
def test_ex1_list_v1_items_db_queries(client, django_assert_num_queries):
    ItemFactory.create_batch(10)

    # Two queries
    # COUNT
    # SELECT 
    with django_assert_num_queries(2):
        response = client.get('/api/v1/inventory/items/')

    assert response.status_code == 200
