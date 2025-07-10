# test_routes.py
import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch

from src.main.routes import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)

@pytest.fixture
def client():
    return TestClient(app)

def test_consolidate_success(client):
    with patch('src.main.routes.fetch_canvas_data', return_value=[{'id': 1}]), \
         patch('src.main.routes.fetch_student_info_data', return_value=[{'id': 2}]), \
         patch('src.main.routes.normalize_canvas', side_effect=lambda x: x), \
         patch('src.main.routes.normalize_student_info', side_effect=lambda x: x), \
         patch('src.main.routes.mock_upsert_student') as mock_upsert:
        response = client.get("/consolidate")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
        assert data["records_processed"] == 2
        assert mock_upsert.call_count == 2

def test_summary_success(client):
    with patch('src.main.routes.mock_get_summary', return_value=[{"course": "Math", "engagement": 90}]):
        response = client.get("/summary")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
        assert isinstance(data["summary"], list)

def test_summary_error(client):
    with patch('src.main.routes.mock_get_summary', side_effect=Exception("DB error")):
        response = client.get("/summary")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "error"
        assert "DB error" in data["message"]