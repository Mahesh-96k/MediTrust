import io

import pytest

from app.main import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get("/")

    assert response.status_code == 200

    data = response.get_json()

    assert data["module"] == "Document Intelligence & OCR"
    assert data["status"] == "running"


def test_health(client):
    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "healthy"


def test_upload_without_file(client):
    response = client.post("/upload")

    assert response.status_code == 400

    data = response.get_json()

    assert data["error"] == "No file provided."


def test_process_without_file(client):
    response = client.post("/process")

    assert response.status_code == 400

    data = response.get_json()

    assert data["error"] == "No file provided."


def test_process_unsupported_file(client):
    response = client.post(
        "/process",
        data={
            "file": (
                io.BytesIO(b"not a medical document"),
                "malware.exe",
            )
        },
        content_type="multipart/form-data",
    )

    assert response.status_code == 400

    data = response.get_json()

    assert "Unsupported file type" in data["error"]