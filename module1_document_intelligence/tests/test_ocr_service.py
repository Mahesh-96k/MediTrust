from pathlib import Path

from PIL import Image, ImageDraw

from app.services.ocr_service import (
    extract_text_from_image,
    extract_text_from_images,
)


def create_test_image(path: Path):
    image = Image.new("RGB", (800, 300), "white")

    draw = ImageDraw.Draw(image)

    draw.text(
        (50, 100),
        "Patient Name: John Smith",
        fill="black",
    )

    draw.text(
        (50, 160),
        "Blood Pressure: 120/80",
        fill="black",
    )

    image.save(path)
    image.close()


def test_extract_text_from_image(tmp_path):
    image_path = tmp_path / "medical_report.png"

    create_test_image(image_path)

    text = extract_text_from_image(str(image_path))

    assert isinstance(text, str)
    assert "Patient" in text
    assert "Blood Pressure" in text


def test_extract_text_from_images(tmp_path):
    image_path_1 = tmp_path / "page_1.png"
    image_path_2 = tmp_path / "page_2.png"

    create_test_image(image_path_1)
    create_test_image(image_path_2)

    text = extract_text_from_images([
        str(image_path_1),
        str(image_path_2),
    ])

    assert isinstance(text, str)
    assert text.count("Patient") >= 2


def test_missing_image():
    missing_path = "does_not_exist.png"

    try:
        extract_text_from_image(missing_path)
        assert False
    except FileNotFoundError:
        assert True