from fastapi.testclient import TestClient
from main import app
import os
import time
from sqlalchemy import create_engine
import pytest

client = TestClient(app)

from app.models import Base  # import your SQLAlchemy Base

@pytest.fixture(scope="session", autouse=True)
def wait_for_db():
    url = os.getenv("DATABASE_URL")
    engine = create_engine(url)

    # Wait for DB to be ready
    start = time.time()
    timeout = 30
    while True:
        try:
            conn = engine.connect()
            conn.close()
            break
        except Exception:
            if time.time() - start > timeout:
                raise TimeoutError("Database did not become available in time")
            time.sleep(1)

    # Create all tables
    Base.metadata.create_all(engine)


def test_register_and_login():
    response = client.post("/register", json={
        "username": "tester",
        "email": "tester@example.com",
        "password": "TestPass123"
    })
    assert response.status_code == 200

    # Login success
    response = client.post("/login", json={
        "username": "tester",
        "password": "TestPass123"
    })
    assert response.status_code == 200
    assert "Welcome, tester" in response.json()["message"]

    # Login failure
    response = client.post("/login", json={
        "username": "tester",
        "password": "wrongpass"
    })
    assert response.status_code == 400
