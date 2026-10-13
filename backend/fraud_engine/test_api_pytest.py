
import app as fraud_api


def test_home_endpoint():
    client = fraud_api.app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "running"
    assert "analyze" in data["endpoints"]


def test_health_endpoint():
    client = fraud_api.app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_analyze_rejects_missing_json():
    client = fraud_api.app.test_client()

    response = client.post("/analyze")

    assert response.status_code == 400
    assert response.get_json()["success"] is False


def test_analyze_rejects_missing_required_fields():
    client = fraud_api.app.test_client()

    response = client.post(
        "/analyze",
        json={
            "report_number": "MR9001",
            "patient_id": "P50001",
        },
    )

    assert response.status_code == 400
    data = response.get_json()
    assert data["success"] is False
    assert "patient_name" in data["missing_fields"]
