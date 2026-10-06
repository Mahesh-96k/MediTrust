from io import BytesIO

import pytest
from werkzeug.datastructures import FileStorage

from app.services.upload_service import save_uploaded_file


def create_file(filename, content=b"test medical document"):
    return FileStorage(
        stream=BytesIO(content),
        filename=filename,
        content_type="application/octet-stream",
    )


def test_upload_pdf(tmp_path, monkeypatch):
    import app.services.upload_service as upload_service

    monkeypatch.setattr(upload_service, "UPLOAD_FOLDER", tmp_path)

    file = create_file("medical_report.pdf")

    saved_path = save_uploaded_file(file)

    assert tmp_path.joinpath("medical_report.pdf").exists()
    assert saved_path.endswith("medical_report.pdf")


def test_upload_jpg(tmp_path, monkeypatch):
    import app.services.upload_service as upload_service

    monkeypatch.setattr(upload_service, "UPLOAD_FOLDER", tmp_path)

    file = create_file("prescription.jpg")

    saved_path = save_uploaded_file(file)

    assert tmp_path.joinpath("prescription.jpg").exists()
    assert saved_path.endswith("prescription.jpg")


def test_reject_executable_file():
    file = create_file("malware.exe")

    with pytest.raises(ValueError, match="Unsupported file type"):
        save_uploaded_file(file)


def test_reject_large_file():
    large_content = b"x" * (11 * 1024 * 1024)

    file = create_file(
        "large_report.pdf",
        large_content,
    )

    with pytest.raises(ValueError, match="10 MB"):
        save_uploaded_file(file)