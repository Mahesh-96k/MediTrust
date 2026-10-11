from medical_report import MedicalReport

from duplicate.duplicate_detector import detect_duplicate_report


def create_report(report_number):
    return MedicalReport(
        report_number=report_number,
        patient_id="P10001",
        patient_name="Rahul Kumar",
        report_date="2026-09-20",
        doctor="Dr. Sharma",
        hospital="ABC Hospital",
        diagnosis="Diabetes",
        tests=[]
    )


# Previously stored reports
stored_reports = [
    create_report("MR1001"),
    create_report("MR1002"),
    create_report("MR1003")
]


# TEST 1: Duplicate report number
new_report = create_report("MR1002")

results = detect_duplicate_report(
    new_report,
    stored_reports
)

print("TEST 1 - DUPLICATE REPORT")
print("-------------------------")

if results:
    for result in results:
        print(result)
else:
    print("FAIL: Duplicate report was not detected.")


# TEST 2: New report number
new_report = create_report("MR1004")

results = detect_duplicate_report(
    new_report,
    stored_reports
)

print("\nTEST 2 - NEW REPORT")
print("-------------------")

if not results:
    print("PASS: No duplicate detected.")
else:
    for result in results:
        print(result)


# TEST 3: Duplicate with different letter case
new_report = create_report("mr1001")

results = detect_duplicate_report(
    new_report,
    stored_reports
)

print("\nTEST 3 - CASE-INSENSITIVE DUPLICATE")
print("-----------------------------------")

if results:
    for result in results:
        print(result)
else:
    print("FAIL: Duplicate report was not detected.")