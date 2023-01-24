"""
Conftest
"""
import pytest
from flask.testing import FlaskClient

from main import app


@pytest.fixture
def client() -> FlaskClient:
    """
    client
    :return:
    """
    with app.test_client() as test_client:
        with app.app_context():
            yield test_client
