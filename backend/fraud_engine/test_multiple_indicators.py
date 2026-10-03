from medical_report import MedicalReport, TestResult

from fraud_engine import analyze_report


# Previously stored report
stored_report = MedicalReport(
    report_number="MR3001",
    patient_id="P30001",
    patient_name="Rahul Kumar",
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


# Intentionally problematic report
suspicious_report = MedicalReport(
    report_number="MR3001",          # Duplicate
    patient_id="ABC123",             # Invalid format
    patient_name="Rohan Kumar",      # Inconsistent
    report_date="2030-09-20",        # Future date
    doctor="Dr. Sharma",
    hospital="ABC Hospital",
    diagnosis="Diabetes",
    tests=[
        TestResult(
            name="Glucose",
            value=450,
            reference_min=70,
            reference_max=140,
            unit="mg/dL"
        )
    ]
)


stored_reports = [
    stored_report
]


stored_patient = {
    "patient_id": "P30001",
    "patient_name": "Rahul Kumar"
}


results = analyze_report(
    report=suspicious_report,
    stored_reports=stored_reports,
    stored_patient=stored_patient
)


print("MULTIPLE INDICATORS TEST")
print("========================")

print("Summary:", results.summary())
print("Total indicators:", results.total_indicators)
print()


for index, indicator in enumerate(
    results.indicators,
    start=1
):
    print(f"Indicator {index}")
    print("--------------")

    print("Type:", indicator.get("type"))
    print("Category:", indicator.get("category"))
    print("Severity:", indicator.get("severity"))
    print("Field:", indicator.get("field"))
    print("Reason:", indicator.get("reason"))

    print()