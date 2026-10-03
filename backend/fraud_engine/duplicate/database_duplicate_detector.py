from typing import List

from medical_report import MedicalReport
from repository import report_exists


def detect_database_duplicate(
    report: MedicalReport
) -> List[dict]:
    indicators = []

    if report_exists(report.report_number):
        indicators.append({
            "type": "DUPLICATE_REPORT",
            "field": "report_number",
            "report_number": report.report_number,
            "reason": (
                "A report with the same report number "
                "already exists in the database."
            )
        })

    return indicators