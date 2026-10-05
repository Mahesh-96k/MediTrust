from pathlib import Path

from app.services.preprocessing_service import process_document
from app.services.ocr_service import extract_text_from_images
from app.services.text_cleaning_service import clean_ocr_text
from app.services.medical_extraction_service import (
    extract_medical_information,
)


def process_medical_document(file_path: str) -> dict:
    """
    Run the complete document intelligence pipeline.

    Pipeline:
        Document
        → Preprocessing
        → OCR
        → Text Cleaning
        → Medical Information Extraction
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Document not found: {file_path}"
        )

    # Step 1: Preprocess the document.
    processed_files = process_document(file_path)

    # Step 2: Extract text using OCR.
    raw_text = extract_text_from_images(processed_files)

    # Step 3: Clean OCR text.
    cleaned_text = clean_ocr_text(raw_text)

    # Step 4: Extract structured medical information.
    medical_information = extract_medical_information(
        cleaned_text
    )

    return {
        "file": str(path),
        "processed_files": processed_files,
        "raw_text": raw_text,
        "cleaned_text": cleaned_text,
        "medical_information": medical_information,
    }