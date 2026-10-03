from typing import List
from medical_report import MedicalReport

REQUIRED_FIELDS = [
    "report_number",
    "patient_id",
    "patient_name",
    "report_date",
    "doctor",
    "hospital",
    "diagnosis",
    "tests"
]


def validate_required_fields(report: MedicalReport) -> List[dict]:
    """
    Check whether required medical report fields are present.

    Returns:
        A list of validation indicators.
        An empty list means no missing required fields were found.
    """

    indicators = []

    for field_name in REQUIRED_FIELDS:
        value = getattr(report, field_name, None)

        if value is None:
            indicators.append({
                "type": "MISSING_FIELD",
                "field": field_name,
                "reason": f"Required field '{field_name}' is missing."
            })

        elif isinstance(value, str) and not value.strip():
            indicators.append({
                "type": "MISSING_FIELD",
                "field": field_name,
                "reason": f"Required field '{field_name}' is empty."
            })

        elif field_name == "tests" and not value:
            indicators.append({
                "type": "MISSING_FIELD",
                "field": field_name,
                "reason": "No laboratory test results were provided."
            })

    return indicators