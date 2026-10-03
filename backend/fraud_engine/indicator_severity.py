INDICATOR_SEVERITY = {

    # Report structure
    "MISSING_FIELD": "MEDIUM",

    # Patient
    "INVALID_PATIENT_ID": "MEDIUM",
    "PATIENT_ID_INCONSISTENCY": "HIGH",
    "PATIENT_INFORMATION_INCONSISTENCY": "HIGH",

    # Date
    "MISSING_REPORT_DATE": "MEDIUM",
    "INVALID_REPORT_DATE": "MEDIUM",
    "FUTURE_REPORT_DATE": "HIGH",

    # Laboratory
    "MISSING_TEST_NAME": "MEDIUM",
    "MISSING_TEST_VALUE": "MEDIUM",
    "INVALID_TEST_VALUE": "MEDIUM",
    "MISSING_REFERENCE_RANGE": "LOW",
    "INVALID_REFERENCE_RANGE": "MEDIUM",
    "ABNORMAL_TEST_VALUE": "MEDIUM",

    # Duplicate
    "DUPLICATE_REPORT": "HIGH",
    "SIMILAR_REPORT": "MEDIUM"
}


def get_indicator_severity(indicator_type: str) -> str:
    """
    Return the configured severity for an indicator.

    Unknown indicator types are assigned LOW severity
    by default.
    """

    return INDICATOR_SEVERITY.get(
        indicator_type,
        "LOW"
    )