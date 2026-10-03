from medical_report import MedicalReport, TestResult

from fraud_engine import analyze_report


report = MedicalReport(
    report_number="MR2001",
    patient_id="P20001",
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
        )
    ]
)


results = analyze_report(
    report=report,
    stored_reports=[],
    stored_patient=None
)


print("CLEAN MEDICAL REPORT TEST")
print("=========================")

print("Summary:", results.summary())
print("Total indicators:", results.total_indicators)

if not results.has_issues:
    print("PASS: Clean report produced no indicators.")
else:
    print("FAIL: Unexpected indicators detected.")

    for indicator in results.indicators:
        print(indicator)