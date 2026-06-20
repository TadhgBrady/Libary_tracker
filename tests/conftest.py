import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.interfaces.api.deps import get_db
from .mock.fake_db import override_get_db


@pytest.fixture(scope="function")
def client():
    app.dependency_overrides[get_db] = override_get_db

    yield TestClient(app)

    app.dependency_overrides.clear()