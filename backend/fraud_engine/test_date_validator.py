from medical_report import MedicalReport

from validation.date_validator import validate_report_date


def create_report(report_date):
    return MedicalReport(
        report_number="MR1001",
        patient_id="P10001",
        patient_name="Rahul Kumar",
        report_date=report_date,
        doctor="Dr. Sharma",
        hospital="ABC Hospital",
        diagnosis="Diabetes",
        tests=[]
    )


# =========================================
# TEST 1: Valid date
# =========================================

report = create_report("2026-09-20")

results = validate_report_date(report)

print("TEST 1 - VALID DATE")
print("-------------------")

if not results:
    print("PASS: Report date is valid.")
else:
    for result in results:
        print(result)


# =========================================
# TEST 2: Missing date
# =========================================

report = create_report("")

results = validate_report_date(report)

print("\nTEST 2 - MISSING DATE")
print("---------------------")

for result in results:
    print(result)


# =========================================
# TEST 3: Invalid format
# =========================================

report = create_report("20/09/2026")

results = validate_report_date(report)

print("\nTEST 3 - INVALID FORMAT")
print("-----------------------")

for result in results:
    print(result)


# =========================================
# TEST 4: Impossible date
# =========================================

report = create_report("2026-02-30")

results = validate_report_date(report)

print("\nTEST 4 - IMPOSSIBLE DATE")
print("------------------------")

for result in results:
    print(result)


# =========================================
# TEST 5: Future date
# =========================================

report = create_report("2030-09-20")

results = validate_report_date(report)

print("\nTEST 5 - FUTURE DATE")
print("--------------------")

for result in results:
    print(result)