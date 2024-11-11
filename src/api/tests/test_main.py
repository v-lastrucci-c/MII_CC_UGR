from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    payload = {"message": "test message"}
    response = client.post("/api/root", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data == {"message": "Servicio FastAPI en desarrollo..."}
