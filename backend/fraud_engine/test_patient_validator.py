from medical_report import MedicalReport, TestResult

from validation.patient_validator import (
    validate_patient_id,
    validate_patient_consistency
)


def create_report(patient_id, patient_name):
    return MedicalReport(
        report_number="MR1001",
        patient_id=patient_id,
        patient_name=patient_name,
        report_date="2026-09-20",
        doctor="Dr. Sharma",
        hospital="ABC Hospital",
        diagnosis="Diabetes",
        tests=[
            TestResult(
                name="Glucose",
                value=120,
                reference_min=70,
                reference_max=140,
                unit="mg/dL"
            )
        ]
    )


# -------------------------------------------------
# TEST 1: Valid patient ID
# -------------------------------------------------

report = create_report("P10001", "Rahul Kumar")

results = validate_patient_id(report)

print("TEST 1 - VALID PATIENT ID")
print("-------------------------")

if not results:
    print("PASS: Patient ID is valid.")
else:
    for result in results:
        print(result)


# -------------------------------------------------
# TEST 2: Invalid patient ID
# -------------------------------------------------

report = create_report("ABC123", "Rahul Kumar")

results = validate_patient_id(report)

print("\nTEST 2 - INVALID PATIENT ID")
print("---------------------------")

for result in results:
    print(result)


# -------------------------------------------------
# TEST 3: Consistent patient information
# -------------------------------------------------

report = create_report("P10001", "Rahul Kumar")

stored_patient = {
    "patient_id": "P10001",
    "patient_name": "Rahul Kumar"
}

results = validate_patient_consistency(
    report,
    stored_patient
)

print("\nTEST 3 - CONSISTENT PATIENT")
print("---------------------------")

if not results:
    print("PASS: Patient information is consistent.")
else:
    for result in results:
        print(result)


# -------------------------------------------------
# TEST 4: Inconsistent patient information
# -------------------------------------------------

report = create_report("P10001", "Rohan Kumar")

results = validate_patient_consistency(
    report,
    stored_patient
)

print("\nTEST 4 - INCONSISTENT PATIENT")
print("-----------------------------")

for result in results:
    print(result)