INDICATOR_CATEGORIES = {

    # Field validation
    "MISSING_FIELD": "REPORT_STRUCTURE",

    # Patient validation
    "INVALID_PATIENT_ID": "PATIENT",
    "PATIENT_ID_INCONSISTENCY": "PATIENT",
    "PATIENT_INFORMATION_INCONSISTENCY": "PATIENT",

    # Date validation
    "MISSING_REPORT_DATE": "DATE",
    "INVALID_REPORT_DATE": "DATE",
    "FUTURE_REPORT_DATE": "DATE",

    # Laboratory validation
    "MISSING_TEST_NAME": "LABORATORY",
    "MISSING_TEST_VALUE": "LABORATORY",
    "INVALID_TEST_VALUE": "LABORATORY",
    "MISSING_REFERENCE_RANGE": "LABORATORY",
    "INVALID_REFERENCE_RANGE": "LABORATORY",
    "ABNORMAL_TEST_VALUE": "LABORATORY",

    # Duplicate detection
    "DUPLICATE_REPORT": "DUPLICATE",
    "SIMILAR_REPORT": "DUPLICATE"
}


def get_indicator_category(indicator_type: str) -> str:
    """
    Return the category associated with an indicator type.

    If the type is not known, return OTHER.
    """

    return INDICATOR_CATEGORIES.get(
        indicator_type,
        "OTHER"
    )