from medical_report import MedicalReport, TestResult

from repository import get_report_by_number
from fraud_engine import analyze_report


print("DATABASE + FRAUD ENGINE INTEGRATION TEST")
print("========================================")


# ------------------------------------------------
# 1. Retrieve an existing report from MySQL
# ------------------------------------------------

stored_report = get_report_by_number("MR5001")


if stored_report is None:
    print("FAIL: MR5001 was not found in MySQL.")
    raise SystemExit


print("\nSTEP 1 - DATABASE REPORT")
print("------------------------")
print("Report retrieved:", stored_report.report_number)
print("Patient:", stored_report.patient_name)


# ------------------------------------------------
# 2. Create a new report for analysis
# ------------------------------------------------

new_report = MedicalReport(
    report_number="MR5002",
    patient_id="P50001",
    patient_name="Anita Sharma",
    report_date="2026-09-20",
    doctor="Dr. Kumar",
    hospital="City Hospital",
    diagnosis="Routine Checkup",
    tests=[
        TestResult(
            name="Glucose",
            value=450,
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


# ------------------------------------------------
# 3. Run fraud analysis
# ------------------------------------------------

results = analyze_report(
    report=new_report,
    stored_reports=[stored_report],
    stored_patient={
        "patient_id": stored_report.patient_id,
        "patient_name": stored_report.patient_name
    }
)


# ------------------------------------------------
# 4. Display results
# ------------------------------------------------

print("\nSTEP 2 - FRAUD ANALYSIS")
print("-----------------------")

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
    print("Reason:", indicator.get("reason"))
    print()