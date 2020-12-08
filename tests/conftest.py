import pytest
from server import app as flask


@pytest.fixture
def app():
    yield flask


@pytest.fixture
def client(app):
    return app.test_client()
