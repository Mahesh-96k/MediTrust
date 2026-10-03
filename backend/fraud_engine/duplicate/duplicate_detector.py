from typing import List

from medical_report import MedicalReport


def detect_duplicate_report(
    report: MedicalReport,
    stored_reports: List[MedicalReport]
) -> List[dict]:
    """
    Check whether the current report already exists
    in the previously stored reports.

    The primary duplicate check is based on report number.

    Args:
        report:
            Current medical report being checked.

        stored_reports:
            Previously processed medical reports.

    Returns:
        A list of duplicate indicators.
        An empty list means no duplicate was found.
    """

    indicators = []

    for stored_report in stored_reports:

        if (
            report.report_number.strip().lower()
            == stored_report.report_number.strip().lower()
        ):
            indicators.append({
                "type": "DUPLICATE_REPORT",
                "field": "report_number",
                "report_number": report.report_number,
                "reason": (
                    "A report with the same report number "
                    "already exists."
                )
            })

    return indicators