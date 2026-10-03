from flask import Flask, jsonify, request

from medical_report import MedicalReport, TestResult
from fraud_engine import analyze_report_from_database


app = Flask(__name__)


def build_medical_report(data: dict) -> MedicalReport:
    tests = []

    for test_data in data.get("tests", []):
        tests.append(
            TestResult(
                name=test_data.get("name", ""),
                value=test_data.get("value"),
                reference_min=test_data.get(
                    "reference_min"
                ),
                reference_max=test_data.get(
                    "reference_max"
                ),
                unit=test_data.get("unit")
            )
        )

    return MedicalReport(
        report_number=data.get("report_number", ""),
        patient_id=data.get("patient_id", ""),
        patient_name=data.get("patient_name", ""),
        report_date=data.get("report_date", ""),
        doctor=data.get("doctor", ""),
        hospital=data.get("hospital", ""),
        diagnosis=data.get("diagnosis", ""),
        tests=tests
    )


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "service": "MediTrust Fraud Detection Engine",
        "status": "running",
        "endpoints": {
            "health": "/health",
            "analyze": "/analyze"
        }
    })

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({
        "status": "ok",
        "service": "MediTrust Fraud Detection Engine"
    })


@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "success": False,
            "error": "JSON request body is required."
        }), 400

    try:
        required_fields = [
            "report_number",
            "patient_id",
            "patient_name",
            "report_date",
            "doctor",
            "hospital",
            "diagnosis"
        ]

        missing_fields = [
            field
            for field in required_fields
            if field not in data
        ]

        if missing_fields:
            return jsonify({
                "success": False,
                "error": "Required API fields are missing.",
                "missing_fields": missing_fields
            }), 400

        report = build_medical_report(data)

        result = analyze_report_from_database(
            report
        )
        return jsonify({
            "success": True,
            "total_indicators": result.total_indicators,
            "has_issues": result.has_issues,
            "summary": result.summary(),
            "indicators": result.indicators
        })

    except Exception as error:
        return jsonify({
            "success": False,
            "error": str(error)
        }), 500


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )