from pathlib import Path
from werkzeug.datastructures import FileStorage

from app.utils.file_validator import (
    is_allowed_file,
    is_file_size_allowed,
)


UPLOAD_FOLDER = Path(__file__).resolve().parents[2] / "uploads"


def save_uploaded_file(file: FileStorage) -> str:
    """
    Validate and save an uploaded medical document.

    Returns:
        str: Saved file path.

    Raises:
        ValueError: If the file is invalid.
    """

    if not file or not file.filename:
        raise ValueError("No file provided.")

    if not is_allowed_file(file.filename):
        raise ValueError(
            "Unsupported file type. "
            "Allowed types: PDF, PNG, JPG, JPEG."
        )

    # Move to the end of the file to determine its size.
    file.seek(0, 2)
    file_size = file.tell()
    file.seek(0)

    if not is_file_size_allowed(file_size):
        raise ValueError("File size exceeds the 10 MB limit.")

    UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)

    filename = Path(file.filename).name
    destination = UPLOAD_FOLDER / filename

    file.save(destination)

    return str(destination)