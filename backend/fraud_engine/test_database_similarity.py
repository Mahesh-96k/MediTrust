from medical_report import MedicalReport
from duplicate.database_similarity_detector import (
    detect_database_similar_reports
)


report = MedicalReport(
    report_number="MR6001",
    patient_id="P50001",
    patient_name="Anita Sharma",
    report_date="2026-09-20",
    doctor="Dr. Mehta",
    hospital="City Hospital",
    diagnosis="Routine Checkup",
    tests=[]
)


print("DATABASE SIMILARITY TEST")
print("========================")

indicators = detect_database_similar_reports(
    report
)

print("\nTOTAL INDICATORS")
print("-----------------")
print(len(indicators))

print("\nINDICATORS")
print("----------")

for indicator in indicators:
    print(
        indicator["type"],
        "|",
        indicator["matched_report_number"],
        "|",
        indicator["similarity_score"]
    )

    print(
        indicator["reason"]
    )