from fastapi.testclient import TestClient
import pytest
from web.main import app


@pytest.fixture
def client():
    return TestClient(app)
