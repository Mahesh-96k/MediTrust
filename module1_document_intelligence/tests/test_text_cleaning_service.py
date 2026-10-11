from app.services.text_cleaning_service import (
    clean_ocr_text,
    normalize_line_breaks,
    normalize_whitespace,
)


def test_normalize_whitespace():
    text = "Patient   Name:\tJohn   Smith"

    result = normalize_whitespace(text)

    assert result == "Patient Name: John Smith"


def test_normalize_line_breaks():
    text = """
    Patient Name: John Smith


    Blood Pressure: 120/80

    """

    result = normalize_line_breaks(text)

    assert result == (
        "Patient Name: John Smith\n"
        "Blood Pressure: 120/80"
    )


def test_clean_ocr_text():
    text = (
        "Patient   Name: John Smith\r\n"
        "\r\n"
        "Blood Pressure:\t120/80\r\n"
    )

    result = clean_ocr_text(text)

    assert result == (
        "Patient Name: John Smith\n"
        "Blood Pressure: 120/80"
    )


def test_empty_text():
    assert clean_ocr_text("") == ""


def test_medical_values_are_preserved():
    text = "Blood Pressure: 120/80\nTemperature: 98.6 F"

    result = clean_ocr_text(text)

    assert "120/80" in result
    assert "98.6 F" in result