from typing import List

from medical_report import MedicalReport
from repository import get_all_medical_reports

from duplicate.similarity_detector import (
    calculate_report_similarity,
    SIMILARITY_THRESHOLD
)


def detect_database_similar_reports(
    report: MedicalReport
) -> List[dict]:
    indicators = []

    stored_reports = get_all_medical_reports()

    for stored_report in stored_reports:

        # Do not compare a report with itself
        if (
            report.report_number.strip().lower()
            == stored_report.report_number.strip().lower()
        ):
            continue

        similarity_score = calculate_report_similarity(
            report,
            stored_report
        )

        if similarity_score >= SIMILARITY_THRESHOLD:
            indicators.append({
                "type": "SIMILAR_REPORT",
                "field": "report_content",
                "report_number": report.report_number,
                "matched_report_number": (
                    stored_report.report_number
                ),
                "similarity_score": round(
                    similarity_score,
                    2
                ),
                "reason": (
                    "The report is highly similar to a "
                    "previously stored report in the database."
                )
            })

    return indicators