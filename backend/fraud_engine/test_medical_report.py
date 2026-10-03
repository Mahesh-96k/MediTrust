from medical_report import MedicalReport, TestResult


report = MedicalReport(
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
            value=145,
            reference_min=70,
            reference_max=140,
            unit="mg/dL"
        )
    ]
)


print("Report Number:", report.report_number)
print("Patient ID:", report.patient_id)
print("Patient Name:", report.patient_name)
print("Diagnosis:", report.diagnosis)

for test in report.tests:
    print("Test:", test.name)
    print("Value:", test.value)
    print("Reference:", test.reference_min, "-", test.reference_max)
    print("Unit:", test.unit)