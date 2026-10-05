from flask import Flask, jsonify, request

from pathlib import Path

from app.services.upload_service import save_uploaded_file

from app.services.document_pipeline_service import (
    process_medical_document,
)

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "module": "Document Intelligence & OCR",
        "status": "running"
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/upload", methods=["POST"])
def upload_document():
    if "file" not in request.files:
        return jsonify({
            "error": "No file provided."
        }), 400

    file = request.files["file"]

    try:
        saved_path = save_uploaded_file(file)

        return jsonify({
            "message": "File uploaded successfully.",
            "filename": file.filename,
            "path": saved_path
        }), 201

    except ValueError as error:
        return jsonify({
            "error": str(error)
        }), 400

    except Exception:
        return jsonify({
            "error": "An unexpected error occurred while uploading the file."
        }), 500

@app.route("/process", methods=["POST"])
def process_document():
    if "file" not in request.files:
        return jsonify({
            "error": "No file provided."
        }), 400

    file = request.files["file"]

    try:
        saved_path = save_uploaded_file(file)

        result = process_medical_document(saved_path)

        processed_files = [
        Path(file_path).name
        for file_path in result["processed_files"]
        ]

        return jsonify({
        "message": "Document processed successfully.",
        "filename": file.filename,
        "medical_information": result["medical_information"],
        "processed_files": processed_files,
        }), 200

    except ValueError as error:
        return jsonify({
            "error": str(error)
        }), 400

    except FileNotFoundError as error:
        return jsonify({
            "error": str(error)
        }), 404

    except Exception:
        return jsonify({
            "error": "An unexpected error occurred while processing the document."
        }), 500

if __name__ == "__main__":
    app.run(debug=True)