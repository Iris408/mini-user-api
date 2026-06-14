from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "mini-user-api",
    }

def test_openapi_schema_available():
    response = client.get("/openapi.json")

    assert response.status_code == 200
    assert "openapi" in response.json()    