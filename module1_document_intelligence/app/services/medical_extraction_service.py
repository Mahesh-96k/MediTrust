import re


def extract_patient_name(text: str) -> str | None:
    """
    Extract patient name from common medical document formats.
    """
    patterns = [
    r"Full\s*name\s*of\s*patient\s*[:\-]\s*(.+)",
    r"Patient\s*Name\s*[:\-]\s*(.+)",
    r"Patient\s*[:\-]\s*(.+)",
    r"Name\s*[:\-]\s*(.+)",
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)

        if match:
            return match.group(1).strip()

    return None

def extract_patient_age(text: str) -> str | None:
    """
    Extract patient age from common medical document formats.
    """
    patterns = [
        r"Age\s*of\s*patient\s*[:\-]\s*(\d+)\s*years?\s*old",
        r"Age\s*of\s*patient\s*[:\-]\s*(\d+)",
        r"Patient\s*Age\s*[:\-]\s*(\d+)",
        r"Age\s*[:\-]\s*(\d+)",
    ]

    for pattern in patterns:
        match = re.search(
            pattern,
            text,
            re.IGNORECASE,
        )

        if match:
            return match.group(1)

    return None

def extract_doctor_name(text: str) -> str | None:
    """
    Extract doctor name from common medical document formats.
    """
    patterns = [
        r"Full\s*name\s*of\s*doctor\s*[:\-]\s*(.+)",
        r"Doctor\s*Name\s*[:\-]\s*(.+)",
        r"Doctor\s*[:\-]\s*(.+)",
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)

        if match:
            return match.group(1).strip()

    return None

def extract_hospital_name(text: str) -> str | None:
    """
    Extract hospital or clinic name and address.
    """
    patterns = [
        r"Hospital\s*/\s*Clinic\s*name\s*and\s*address\s*[:\-]\s*(.+)",
        r"Hospital\s*name\s*[:\-]\s*(.+)",
        r"Clinic\s*name\s*[:\-]\s*(.+)",
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)

        if match:
            return match.group(1).strip()

    return None

def extract_diagnoses(text: str) -> list[str]:
    """
    Extract numbered diagnoses listed under a Diagnosis section.
    """
    match = re.search(
        r"Diagnosis\s*:\s*(.*?)(?=\n\s*(?:SECTION|[A-Z][A-Z\s']+?:)|\Z)",
        text,
        re.IGNORECASE | re.DOTALL,
    )

    if not match:
        return []

    diagnosis_section = match.group(1)

    diagnoses = []

    for line in diagnosis_section.splitlines():
        line = line.strip()

        numbered_match = re.match(
            r"^\d+\.\s*(.+)$",
            line,
        )

        if numbered_match:
            diagnoses.append(
                numbered_match.group(1).strip()
            )

    return diagnoses

def extract_date(text: str) -> str | None:
    """
    Extract common numeric and textual date formats.
    """
    patterns = [
        # Examples: 20/07/2015, 20-07-2015
        r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b",

        # Examples: 2015/07/20, 2015-07-20
        r"\b\d{4}[/-]\d{1,2}[/-]\d{1,2}\b",

        # Examples: 20 July 2015, 20 June 2015
        r"\b\d{1,2}\s+"
        r"(?:January|February|March|April|May|June|July|August|"
        r"September|October|November|December)"
        r"\s+\d{4}\b",
    ]

    for pattern in patterns:
        match = re.search(
            pattern,
            text,
            re.IGNORECASE,
        )

        if match:
            return match.group(0)

    return None


def extract_blood_pressure(text: str) -> str | None:
    """
    Extract blood pressure values such as 120/80.
    """
    pattern = r"(?:Blood\s*Pressure|BP)\s*[:\-]?\s*(\d{2,3}/\d{2,3})"

    match = re.search(pattern, text, re.IGNORECASE)

    if match:
        return match.group(1)

    return None


def extract_temperature(text: str) -> str | None:
    """
    Extract body temperature.
    """
    pattern = (
        r"(?:Temperature|Temp)"
        r"\s*[:\-]?\s*(\d{2,3}(?:\.\d+)?)\s*°?\s*([CF])?"
    )

    match = re.search(pattern, text, re.IGNORECASE)

    if match:
        value = match.group(1)
        unit = match.group(2)

        if unit:
            return f"{value} {unit.upper()}"

        return value

    return None


def extract_medical_information(text: str) -> dict:
    """
    Extract structured medical information from cleaned OCR text.
    """
    return {
    "patient_name": extract_patient_name(text),
    "patient_age": extract_patient_age(text),
    "doctor_name": extract_doctor_name(text),
    "hospital_name": extract_hospital_name(text),
    "date": extract_date(text),
    "blood_pressure": extract_blood_pressure(text),
    "temperature": extract_temperature(text),
    "diagnoses": extract_diagnoses(text),
}