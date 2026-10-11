from medical_report import MedicalReport

from duplicate.similarity_detector import (
    calculate_report_similarity,
    detect_similar_reports
)


def create_report(
    report_number,
    patient_id="P10001",
    patient_name="Rahul Kumar",
    report_date="2026-09-20",
    doctor="Dr. Sharma",
    hospital="ABC Hospital",
    diagnosis="Diabetes"
):
    return MedicalReport(
        report_number=report_number,
        patient_id=patient_id,
        patient_name=patient_name,
        report_date=report_date,
        doctor=doctor,
        hospital=hospital,
        diagnosis=diagnosis,
        tests=[]
    )


# Previously stored report
stored_report = create_report("MR1001")

stored_reports = [stored_report]


# TEST 1: Completely matching report information
new_report = create_report("MR9999")

score = calculate_report_similarity(
    new_report,
    stored_report
)

results = detect_similar_reports(
    new_report,
    stored_reports
)

print("TEST 1 - HIGHLY SIMILAR REPORT")
print("-------------------------------")
print("Similarity score:", score)

if results:
    print("PASS: Similar report detected.")
    for result in results:
        print(result)
else:
    print("FAIL: Similar report was not detected.")


# TEST 2: One field is different
new_report = create_report(
    "MR8888",
    diagnosis="Hypertension"
)

score = calculate_report_similarity(
    new_report,
    stored_report
)

results = detect_similar_reports(
    new_report,
    stored_reports
)

print("\nTEST 2 - ONE DIFFERENT FIELD")
print("-----------------------------")
print("Similarity score:", score)

if results:
    print("PASS: Report is still above similarity threshold.")
    for result in results:
        print(result)
else:
    print("No similar report detected.")


# TEST 3: Multiple fields are different
new_report = create_report(
    "MR7777",
    patient_id="P20002",
    patient_name="Amit Kumar",
    doctor="Dr. Patel",
    hospital="XYZ Hospital",
    diagnosis="Fever"
)

score = calculate_report_similarity(
    new_report,
    stored_report
)

results = detect_similar_reports(
    new_report,
    stored_reports
)

print("\nTEST 3 - DIFFERENT REPORT")
print("-------------------------")
print("Similarity score:", score)

if results:
    print("Similar report detected:")
    for result in results:
        print(result)
else:
    print("PASS: No similar report detected.")