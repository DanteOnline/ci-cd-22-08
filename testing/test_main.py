"""
Test main
"""

import random


def test_get_item(client):
    """
    Test get item
    :param client:
    :return:
    """
    random_id = random.randint(1,100)
    url = f'/items/{random_id}/'
    response = client.get(url)
    assert response.status_code == 200

    assert response.json['item']['id'] == random_id
