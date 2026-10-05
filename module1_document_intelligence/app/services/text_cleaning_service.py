import re


def normalize_whitespace(text: str) -> str:
    """
    Normalize spaces and tabs while preserving line structure.
    """
    text = re.sub(r"[ \t]+", " ", text)

    return text


def normalize_line_breaks(text: str) -> str:
    """
    Remove unnecessary blank lines and trailing whitespace.
    """
    lines = []

    for line in text.splitlines():
        line = line.strip()

        if line:
            lines.append(line)

    return "\n".join(lines)


def clean_ocr_text(text: str) -> str:
    """
    Clean OCR-generated text while preserving useful medical content.
    """
    if not text:
        return ""

    text = text.replace("\r\n", "\n")
    text = text.replace("\r", "\n")

    text = normalize_whitespace(text)
    text = normalize_line_breaks(text)

    return text.strip()