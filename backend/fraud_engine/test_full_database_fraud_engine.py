from medical_report import MedicalReport, TestResult
from fraud_engine import analyze_report


report = MedicalReport(
    report_number="MR6001",
    patient_id="P50001",
    patient_name="Anita Sharma",
    report_date="2026-09-20",
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


print("FULL DATABASE FRAUD ENGINE TEST")
print("================================")

result = analyze_report(report)

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