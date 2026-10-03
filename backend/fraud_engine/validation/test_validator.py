from typing import List

from medical_report import MedicalReport


def validate_test_results(report: MedicalReport) -> List[dict]:
    """
    Validate laboratory test results.

    Checks:
    1. Test name is present.
    2. Test value is present.
    3. Test value is numeric.
    4. Reference range is available.
    5. Test value is within the configured reference range.
    """

    indicators = []

    for index, test in enumerate(report.tests):

        # -----------------------------------------
        # Check 1: Test name
        # -----------------------------------------

        if not test.name or not test.name.strip():
            indicators.append({
                "type": "MISSING_TEST_NAME",
                "field": f"tests[{index}].name",
                "reason": "Laboratory test name is missing."
            })

        # -----------------------------------------
        # Check 2: Test value
        # -----------------------------------------

        if test.value is None:
            indicators.append({
                "type": "MISSING_TEST_VALUE",
                "field": f"tests[{index}].value",
                "reason": "Laboratory test value is missing."
            })

            continue

        # -----------------------------------------
        # Check 3: Numeric value
        # -----------------------------------------

        try:
            numeric_value = float(test.value)

        except (TypeError, ValueError):
            indicators.append({
                "type": "INVALID_TEST_VALUE",
                "field": f"tests[{index}].value",
                "value": test.value,
                "reason": "Laboratory test value must be numeric."
            })

            continue

        # -----------------------------------------
        # Check 4: Reference range
        # -----------------------------------------

        if (
            test.reference_min is None
            or test.reference_max is None
        ):
            indicators.append({
                "type": "MISSING_REFERENCE_RANGE",
                "field": f"tests[{index}]",
                "test_name": test.name,
                "reason": "Reference range is incomplete or missing."
            })

            continue

        # -----------------------------------------
        # Check 5: Reference range validity
        # -----------------------------------------

        if test.reference_min > test.reference_max:
            indicators.append({
                "type": "INVALID_REFERENCE_RANGE",
                "field": f"tests[{index}]",
                "test_name": test.name,
                "reason": (
                    "Reference minimum cannot be greater "
                    "than reference maximum."
                )
            })

            continue

        # -----------------------------------------
        # Check 6: Value outside range
        # -----------------------------------------

        if (
            numeric_value < test.reference_min
            or numeric_value > test.reference_max
        ):
            indicators.append({
                "type": "ABNORMAL_TEST_VALUE",
                "field": f"tests[{index}].value",
                "test_name": test.name,
                "value": numeric_value,
                "reference_min": test.reference_min,
                "reference_max": test.reference_max,
                "reason": (
                    f"Test value {numeric_value} is outside "
                    f"the configured reference range "
                    f"({test.reference_min} - {test.reference_max})."
                )
            })

    return indicators