from pathlib import Path

import pytest
from PIL import Image

from app.services.preprocessing_service import (
    process_document,
)


def test_preprocess_pdf(tmp_path, monkeypatch):
    import app.services.preprocessing_service as preprocessing_service

    monkeypatch.setattr(
        preprocessing_service,
        "PROCESSED_FOLDER",
        tmp_path,
    )

    # Create a small test PDF.
    import fitz

    pdf_path = tmp_path / "test_report.pdf"

    document = fitz.open()
    page = document.new_page(width=300, height=200)
    page.insert_text((50, 100), "Medical Test Report")
    document.save(pdf_path)
    document.close()

    processed_files = process_document(str(pdf_path))

    assert len(processed_files) == 1

    output_path = Path(processed_files[0])

    assert output_path.exists()
    assert output_path.suffix == ".png"


def test_preprocess_image(tmp_path, monkeypatch):
    import app.services.preprocessing_service as preprocessing_service

    monkeypatch.setattr(
        preprocessing_service,
        "PROCESSED_FOLDER",
        tmp_path,
    )

    image_path = tmp_path / "prescription.jpg"

    image = Image.new("RGB", (100, 100), "white")
    image.save(image_path)

    processed_files = process_document(str(image_path))

    assert len(processed_files) == 1

    output_path = Path(processed_files[0])

    assert output_path.exists()
    assert output_path.suffix == ".png"


def test_missing_document():
    with pytest.raises(FileNotFoundError):
        process_document("does_not_exist.pdf")


def test_unsupported_document(tmp_path):
    txt_path = tmp_path / "report.txt"
    txt_path.write_text("Medical report")

    with pytest.raises(ValueError, match="Unsupported document type"):
        process_document(str(txt_path))