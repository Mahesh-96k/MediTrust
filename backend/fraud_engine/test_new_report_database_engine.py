from medical_report import MedicalReport
from fraud_engine import analyze_report


report = MedicalReport(
    report_number="MR9999",
    patient_id="P90001",
    patient_name="Rahul Sharma",
    report_date="2026-09-20",
    doctor="Dr. Mehta",
    hospital="City Hospital",
    diagnosis="Routine Checkup",
    tests=[]
)


print("NEW REPORT + FRAUD ENGINE TEST")
print("==============================")

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

print("\nSUMMARY")
print("-------")
print(result.summary())