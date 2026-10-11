from typing import List

from medical_report import MedicalReport


SIMILARITY_THRESHOLD = 0.8


def calculate_report_similarity(
    report1: MedicalReport,
    report2: MedicalReport
) -> float:
    """
    Calculate similarity between two medical reports.

    The report number is intentionally excluded because
    two different report numbers may still belong to
    duplicated or highly similar reports.

    Compared fields:
    - patient ID
    - patient name
    - report date
    - doctor
    - hospital
    - diagnosis

    Returns:
        Similarity score between 0.0 and 1.0.
    """

    fields = [
        "patient_id",
        "patient_name",
        "report_date",
        "doctor",
        "hospital",
        "diagnosis"
    ]

    matches = 0

    for field_name in fields:
        value1 = getattr(report1, field_name, "")
        value2 = getattr(report2, field_name, "")

        value1 = str(value1).strip().lower()
        value2 = str(value2).strip().lower()

        if value1 == value2:
            matches += 1

    return matches / len(fields)


def detect_similar_reports(
    report: MedicalReport,
    stored_reports: List[MedicalReport]
) -> List[dict]:
    """
    Compare a report against previously stored reports.

    Reports whose similarity score reaches the configured
    threshold are returned as similarity indicators.
    """

    indicators = []

    for stored_report in stored_reports:

        similarity_score = calculate_report_similarity(
            report,
            stored_report
        )

        if similarity_score >= SIMILARITY_THRESHOLD:

            indicators.append({
                "type": "SIMILAR_REPORT",
                "field": "report_content",
                "report_number": report.report_number,
                "matched_report_number": stored_report.report_number,
                "similarity_score": round(similarity_score, 2),
                "reason": (
                    "The report is highly similar to a "
                    "previously stored report."
                )
            })

    return indicators