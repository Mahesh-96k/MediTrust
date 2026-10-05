from pathlib import Path

import pytesseract
from PIL import Image

TESSERACT_PATH = Path(
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

if TESSERACT_PATH.exists():
    pytesseract.pytesseract.tesseract_cmd = str(
        TESSERACT_PATH
    )

def extract_text_from_image(file_path: str) -> str:
    """
    Extract text from a single image using Tesseract OCR.

    Args:
        file_path: Path to the image file.

    Returns:
        Extracted text as a string.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Image not found: {file_path}"
        )

    image = Image.open(path)

    try:
        text = pytesseract.image_to_string(image)
        return text.strip()
    finally:
        image.close()


def extract_text_from_images(file_paths: list[str]) -> str:
    """
    Extract and combine OCR text from multiple images.

    Args:
        file_paths: List of image file paths.

    Returns:
        Combined extracted text.
    """
    extracted_text = []

    for file_path in file_paths:
        text = extract_text_from_image(file_path)

        if text:
            extracted_text.append(text)

    return "\n\n".join(extracted_text)