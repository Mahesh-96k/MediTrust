from flask import Flask, request, jsonify
from main import analyze_report

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Medical Fraud AI Risk API",
        "module": "Module 3 - AI Anomaly & Risk Intelligence",
        "status": "running"
    })


@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "error": "No JSON data received"
            }), 400

        medical_data = data["medical_data"]
        validation_indicators = data["validation_indicators"]

        result = analyze_report(
            medical_data,
            validation_indicators
        )

        result["report_id"] = data.get(
            "report_id",
            "UNKNOWN"
        )

        return jsonify(result)

    except KeyError as error:
        return jsonify({
            "error": f"Missing field: {error}"
        }), 400

    except Exception as error:
        return jsonify({
            "error": str(error)
        }), 500


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )
