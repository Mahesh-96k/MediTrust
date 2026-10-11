from medical_report import MedicalReport, TestResult

from repository import (
    save_medical_report,
    get_report_by_number
)


report = MedicalReport(
    report_number="MR5001",
    patient_id="P50001",
    patient_name="Anita Sharma",
    report_date="2026-09-20",
    doctor="Dr. Kumar",
    hospital="City Hospital",
    diagnosis="Routine Checkup",
    tests=[
        TestResult(
            name="Glucose",
            value=100,
            reference_min=70,
            reference_max=140,
            unit="mg/dL"
        ),
        TestResult(
            name="Hemoglobin",
            value=13.5,
            reference_min=12,
            reference_max=16,
            unit="g/dL"
        )
    ]
)


print("SAVE MEDICAL REPORT TEST")
print("========================")


# TEST 1: Save report
print("\nTEST 1 - SAVE REPORT")
print("--------------------")

result = save_medical_report(report)

if result:
    print("PASS: Medical report saved.")
else:
    print("FAIL: Medical report was not saved.")


# TEST 2: Retrieve report
print("\nTEST 2 - RETRIEVE REPORT")
print("------------------------")

saved_report = get_report_by_number(
    "MR5001"
)

if saved_report:

    print("PASS: Medical report retrieved.")

    print("\nReport:")
    print(saved_report)

    print("\nLaboratory Tests:")

    for test in saved_report.tests:
        print(
            f"- {test.name}: "
            f"{test.value} "
            f"{test.unit} "
            f"(Reference: "
            f"{test.reference_min} - "
            f"{test.reference_max})"
        )

else:
    print("FAIL: Medical report not found.")