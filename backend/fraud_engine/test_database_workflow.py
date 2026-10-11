from medical_report import MedicalReport, TestResult
from fraud_engine import analyze_report_from_database


report = MedicalReport(
    report_number="MR7001",
    patient_id="P50001",
    patient_name="Anita Sharma",
    report_date="2026-09-25",
    doctor="Dr. Mehta",
    hospital="City Hospital",
    diagnosis="Routine Checkup",
    tests=[
        TestResult(
            name="Glucose",
            value=100.0,
            reference_min=70.0,
            reference_max=140.0,
            unit="mg/dL"
        ),
        TestResult(
            name="Hemoglobin",
            value=13.5,
            reference_min=12.0,
            reference_max=16.0,
            unit="g/dL"
        )
    ]
)


print("DATABASE WORKFLOW TEST")
print("======================")

result = analyze_report_from_database(
    report
)

print("\nTOTAL INDICATORS")
print("-----------------")
print(result.total_indicators)

print("\nINDICATORS")
print("----------")

for indicator in result.indicators:

    print(
        indicator["type"],
        "|",
        indicator["category"],
        "|",
        indicator["severity"]
    )

    if "similarity_score" in indicator:
        print(
            "   Similarity:",
            indicator["similarity_score"]
        )

    print(
        "   Reason:",
        indicator["reason"]
    )

print("\nSUMMARY")
print("-------")
print(result.summary())