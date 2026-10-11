from medical_report import MedicalReport, TestResult

from fraud_engine import analyze_report


# Previously stored report
stored_report = MedicalReport(
    report_number="MR1001",
    patient_id="P10001",
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


# Current report
current_report = MedicalReport(
    report_number="MR1002",
    patient_id="P10001",
    patient_name="Rahul Kumar",
    report_date="2026-09-20",
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
    "patient_id": "P10001",
    "patient_name": "Rahul Kumar"
}


results = analyze_report(
    current_report,
    stored_reports,
    stored_patient
)


print("MEDICAL REPORT FRAUD ANALYSIS")
print("=============================")

if not results.has_issues:
    print(results.summary())

else:
    print("Summary:", results.summary())
    print("Total indicators found:", results.total_indicators)
    print()

    for index, result in enumerate(
        results.indicators,
        start=1
    ):
        print(f"Indicator {index}")
        print("--------------")

        for key, value in result.items():
            print(f"{key}: {value}")

        print()