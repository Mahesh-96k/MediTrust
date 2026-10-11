from medical_report import MedicalReport, TestResult

from validation.test_validator import validate_test_results


def create_report(tests):
    return MedicalReport(
        report_number="MR1001",
        patient_id="P10001",
        patient_name="Rahul Kumar",
        report_date="2026-09-20",
        doctor="Dr. Sharma",
        hospital="ABC Hospital",
        diagnosis="Diabetes",
        tests=tests
    )


# =========================================
# TEST 1: Valid laboratory value
# =========================================

report = create_report([
    TestResult(
        name="Glucose",
        value=120,
        reference_min=70,
        reference_max=140,
        unit="mg/dL"
    )
])

results = validate_test_results(report)

print("TEST 1 - VALID TEST VALUE")
print("-------------------------")

if not results:
    print("PASS: Laboratory value is valid.")
else:
    for result in results:
        print(result)


# =========================================
# TEST 2: Value above reference range
# =========================================

report = create_report([
    TestResult(
        name="Glucose",
        value=450,
        reference_min=70,
        reference_max=140,
        unit="mg/dL"
    )
])

results = validate_test_results(report)

print("\nTEST 2 - ABNORMAL TEST VALUE")
print("-----------------------------")

for result in results:
    print(result)


# =========================================
# TEST 3: Missing test name
# =========================================

report = create_report([
    TestResult(
        name="",
        value=120,
        reference_min=70,
        reference_max=140,
        unit="mg/dL"
    )
])

results = validate_test_results(report)

print("\nTEST 3 - MISSING TEST NAME")
print("--------------------------")

for result in results:
    print(result)


# =========================================
# TEST 4: Missing reference range
# =========================================

report = create_report([
    TestResult(
        name="Glucose",
        value=120,
        reference_min=None,
        reference_max=None,
        unit="mg/dL"
    )
])

results = validate_test_results(report)

print("\nTEST 4 - MISSING REFERENCE RANGE")
print("--------------------------------")

for result in results:
    print(result)


# =========================================
# TEST 5: Invalid reference range
# =========================================

report = create_report([
    TestResult(
        name="Glucose",
        value=120,
        reference_min=140,
        reference_max=70,
        unit="mg/dL"
    )
])

results = validate_test_results(report)

print("\nTEST 5 - INVALID REFERENCE RANGE")
print("--------------------------------")

for result in results:
    print(result)