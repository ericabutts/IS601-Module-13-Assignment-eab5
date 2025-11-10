from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_register_and_login():
    # Register user
    response = client.post("/register", json={
        "username": "tester",
        "email": "tester@example.com",
        "password": "TestPass123"
    })
    assert response.status_code == 200

    # Login success
    response = client.post("/login?username=tester&password=TestPass123")
    assert response.status_code == 200

    # Login failure
    response = client.post("/login?username=tester&password=wrongpass")
    assert response.status_code == 400
