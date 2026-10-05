from pathlib import Path

from app.services.document_pipeline_service import (
    process_medical_document,
)


def test_process_medical_document(tmp_path, monkeypatch):
    import app.services.preprocessing_service as preprocessing_service

    monkeypatch.setattr(
        preprocessing_service,
        "PROCESSED_FOLDER",
        tmp_path,
    )

    import fitz

    pdf_path = tmp_path / "medical_report.pdf"

    document = fitz.open()
    page = document.new_page(width=400, height=300)

    page.insert_text(
        (50, 80),
        "Patient Name: John Smith",
    )

    page.insert_text(
        (50, 120),
        "Age of patient: 55 years old",
    )

    page.insert_text(
        (50, 160),
        "Full name of doctor: Tan Ah Moi",
    )

    page.insert_text(
        (50, 200),
        "Diagnosis:",
    )

    page.insert_text(
        (50, 240),
        "1. Dementia",
    )

    document.save(pdf_path)
    document.close()

    result = process_medical_document(
        str(pdf_path)
    )

    medical_information = result["medical_information"]

    assert medical_information["patient_name"] == "John Smith"
    assert medical_information["patient_age"] == "55"
    assert medical_information["doctor_name"] == "Tan Ah Moi"
    assert medical_information["diagnoses"] == ["Dementia"]

    assert result["raw_text"]
    assert result["cleaned_text"]
    assert len(result["processed_files"]) == 1


def test_process_missing_document():
    missing_path = "does_not_exist.pdf"

    try:
        process_medical_document(missing_path)
        assert False
    except FileNotFoundError:
        assert True