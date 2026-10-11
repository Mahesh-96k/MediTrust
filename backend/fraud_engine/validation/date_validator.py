from datetime import datetime, date
from typing import List

from medical_report import MedicalReport


DATE_FORMAT = "%Y-%m-%d"


def validate_report_date(report: MedicalReport) -> List[dict]:
    """
    Validate the report date.

    Checks:
    1. Date is present.
    2. Date follows YYYY-MM-DD format.
    3. Date actually exists.
    4. Date is not in the future.
    """

    indicators = []

    report_date = report.report_date

    # -----------------------------------------
    # Check 1: Missing date
    # -----------------------------------------

    if not report_date or not report_date.strip():
        indicators.append({
            "type": "MISSING_REPORT_DATE",
            "field": "report_date",
            "reason": "Report date is missing."
        })

        return indicators

    # -----------------------------------------
    # Check 2 & 3: Format and actual date
    # -----------------------------------------

    try:
        parsed_date = datetime.strptime(
            report_date.strip(),
            DATE_FORMAT
        ).date()

    except ValueError:
        indicators.append({
            "type": "INVALID_REPORT_DATE",
            "field": "report_date",
            "value": report_date,
            "reason": (
                "Report date must be a valid date "
                "in YYYY-MM-DD format."
            )
        })

        return indicators

    # -----------------------------------------
    # Check 4: Future date
    # -----------------------------------------

    if parsed_date > date.today():
        indicators.append({
            "type": "FUTURE_REPORT_DATE",
            "field": "report_date",
            "value": report_date,
            "reason": "Report date cannot be in the future."
        })

    return indicators