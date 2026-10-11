import re
from typing import List, Optional

from medical_report import MedicalReport


PATIENT_ID_PATTERN = r"^P\d{5}$"


def validate_patient_id(report: MedicalReport) -> List[dict]:
    """
    Validate the patient ID of a medical report.

    For the synthetic project dataset, the expected format is:
    P followed by exactly 5 digits.

    Example:
        P10001 -> valid
        P123   -> invalid
    """

    indicators = []

    patient_id = report.patient_id

    # Check if patient ID is missing
    if not patient_id or not patient_id.strip():
        indicators.append({
            "type": "INVALID_PATIENT_ID",
            "field": "patient_id",
            "reason": "Patient ID is missing."
        })

        return indicators

    # Check patient ID format
    if not re.fullmatch(PATIENT_ID_PATTERN, patient_id.strip()):
        indicators.append({
            "type": "INVALID_PATIENT_ID",
            "field": "patient_id",
            "value": patient_id,
            "reason": (
                "Patient ID must contain 'P' followed by exactly 5 digits."
            )
        })

    return indicators


def validate_patient_consistency(
    report: MedicalReport,
    stored_patient: Optional[dict]
) -> List[dict]:
    """
    Compare the current report's patient information
    with a previously stored patient record.

    Example stored_patient:
    {
        "patient_id": "P10001",
        "patient_name": "Rahul Kumar"
    }
    """

    indicators = []

    # No stored record means there is nothing to compare against.
    if stored_patient is None:
        return indicators

    stored_patient_id = stored_patient.get("patient_id")
    stored_patient_name = stored_patient.get("patient_name")

    # Compare patient ID
    if (
        stored_patient_id is not None
        and report.patient_id != stored_patient_id
    ):
        indicators.append({
            "type": "PATIENT_ID_INCONSISTENCY",
            "field": "patient_id",
            "expected": stored_patient_id,
            "found": report.patient_id,
            "reason": "Patient ID does not match the stored patient record."
        })

    # Compare patient name
    if (
        stored_patient_name is not None
        and report.patient_name.strip().lower()
        != stored_patient_name.strip().lower()
    ):
        indicators.append({
            "type": "PATIENT_INFORMATION_INCONSISTENCY",
            "field": "patient_name",
            "expected": stored_patient_name,
            "found": report.patient_name,
            "reason": "Patient name does not match the stored patient record."
        })

    return indicators