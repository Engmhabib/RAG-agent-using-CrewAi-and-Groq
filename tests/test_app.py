
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_upload_pdf():
    response = client.post("/upload_pdf", files={"file": ("test.pdf", b"dummy content")})
    assert response.status_code == 200
    assert "PDF uploaded successfully" in response.json()["message"]

def test_query_pdf():
    response = client.post("/query_pdf", json={"question": "What is this?", "filename": "test.pdf"})
    assert response.status_code == 200
    assert "Dummy response" in response.json()["answer"]
