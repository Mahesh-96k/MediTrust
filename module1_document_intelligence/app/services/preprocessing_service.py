from pathlib import Path

import pymupdf
from PIL import Image, ImageEnhance, ImageOps


PROCESSED_FOLDER = Path(__file__).resolve().parents[2] / "processed"


def preprocess_image(image: Image.Image) -> Image.Image:
    """
    Convert an image to grayscale and enhance its contrast.
    """
    image = ImageOps.grayscale(image)

    contrast = ImageEnhance.Contrast(image)
    image = contrast.enhance(1.5)

    return image


def preprocess_pdf(file_path: Path) -> list[str]:
    """
    Render each PDF page as an image and preprocess it.

    Returns:
        list[str]: Paths of processed page images.
    """
    PROCESSED_FOLDER.mkdir(parents=True, exist_ok=True)

    document = pymupdf.open(file_path)
    processed_files = []

    try:
        for page_number, page in enumerate(document, start=1):
            pixmap = page.get_pixmap(matrix=pymupdf.Matrix(2, 2))
            image = Image.frombytes(
                "RGB",
                [pixmap.width, pixmap.height],
                pixmap.samples,
            )

            image = preprocess_image(image)

            output_path = (
                PROCESSED_FOLDER
                / f"{file_path.stem}_page_{page_number:03d}.png"
            )

            image.save(output_path, "PNG")

            processed_files.append(str(output_path))

    finally:
        document.close()

    return processed_files


def preprocess_image_file(file_path: Path) -> list[str]:
    """
    Open and preprocess a single image file.

    Returns:
        list[str]: Path of the processed image.
    """
    PROCESSED_FOLDER.mkdir(parents=True, exist_ok=True)

    image = Image.open(file_path)
    image = preprocess_image(image)

    output_path = (
        PROCESSED_FOLDER
        / f"{file_path.stem}_processed.png"
    )

    image.save(output_path, "PNG")

    return [str(output_path)]


def process_document(file_path: str) -> list[str]:
    """
    Preprocess a PDF or supported image document.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Document not found: {file_path}"
        )

    extension = path.suffix.lower()

    if extension == ".pdf":
        return preprocess_pdf(path)

    if extension in {".png", ".jpg", ".jpeg"}:
        return preprocess_image_file(path)

    raise ValueError(
        "Unsupported document type. "
        "Allowed types: PDF, PNG, JPG, JPEG."
    )