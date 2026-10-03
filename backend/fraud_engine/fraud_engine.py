from typing import List, Optional

from medical_report import MedicalReport

from analysis_result import AnalysisResult

from repository import get_patient

from indicator_formatter import format_indicators

from validation.field_validator import validate_required_fields
from validation.patient_validator import (
    validate_patient_id,
    validate_patient_consistency
)
from validation.date_validator import validate_report_date
from validation.test_validator import validate_test_results

from duplicate.duplicate_detector import detect_duplicate_report
from duplicate.similarity_detector import detect_similar_reports

from duplicate.database_duplicate_detector import (
    detect_database_duplicate
)

from duplicate.database_similarity_detector import (
    detect_database_similar_reports
)

def analyze_report(
    report: MedicalReport,
    stored_reports: Optional[List[MedicalReport]] = None,
    stored_patient: Optional[dict] = None
) -> AnalysisResult:
    """
    Run all validation and fraud-detection checks
    on a medical report.

    Returns:
        A combined list of validation/fraud indicators.
    """

    if stored_reports is None:
        stored_reports = []

    indicators = []

    # 1. Required field validation
    indicators.extend(
        validate_required_fields(report)
    )

    # 2. Patient ID validation
    indicators.extend(
        validate_patient_id(report)
    )

    # 3. Patient information consistency
    indicators.extend(
        validate_patient_consistency(
            report,
            stored_patient
        )
    )

    # 4. Report date validation
    indicators.extend(
        validate_report_date(report)
    )

    # 5. Laboratory/test result validation
    indicators.extend(
        validate_test_results(report)
    )

    duplicate_indicators = detect_duplicate_report(
        report,
        stored_reports
    )

    database_duplicate_indicators = detect_database_duplicate(
        report
    )

    if duplicate_indicators:
        indicators.extend(duplicate_indicators)
    elif database_duplicate_indicators:
        indicators.extend(database_duplicate_indicators)

    indicators.extend(
        detect_similar_reports(
            report,
            stored_reports
        )
    )

    indicators.extend(
        detect_database_similar_reports(
            report
        )
    )

    formatted_indicators = format_indicators(
        indicators
    )

    return AnalysisResult(
        indicators=formatted_indicators
    )

def analyze_report_from_database(
    report: MedicalReport
) -> AnalysisResult:
    """
    Analyze a medical report using patient information
    stored in the database.

    The function automatically retrieves the stored
    patient record and then runs the fraud engine.
    """

    stored_patient = get_patient(
        report.patient_id
    )

    return analyze_report(
        report=report,
        stored_reports=[],
        stored_patient=stored_patient
    )