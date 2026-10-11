from app.utils.file_validator import (
    is_allowed_file,
    is_file_size_allowed,
)


def test_allowed_pdf():
    assert is_allowed_file("medical_report.pdf") is True


def test_allowed_image():
    assert is_allowed_file("prescription.jpg") is True


def test_rejected_file():
    assert is_allowed_file("malware.exe") is False


def test_file_without_extension():
    assert is_allowed_file("medical_report") is False


def test_allowed_file_size():
    assert is_file_size_allowed(5 * 1024 * 1024) is True


def test_rejected_file_size():
    assert is_file_size_allowed(11 * 1024 * 1024) is False