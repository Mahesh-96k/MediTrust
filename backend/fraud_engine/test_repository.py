from repository import (
    insert_patient,
    get_patient,
    get_report_by_number
)


PATIENT_ID = "P90001"
PATIENT_NAME = "Test Patient"


print("DATABASE REPOSITORY TEST")
print("========================")


# TEST 1: Insert patient
print("\nTEST 1 - INSERT PATIENT")
print("-----------------------")

result = insert_patient(
    PATIENT_ID,
    PATIENT_NAME
)

if result:
    print("PASS: Patient inserted.")
else:
    print("Patient was not inserted.")


# TEST 2: Retrieve patient
print("\nTEST 2 - GET PATIENT")
print("--------------------")

patient = get_patient(PATIENT_ID)

if patient:
    print("PASS: Patient retrieved.")
    print(patient)
else:
    print("FAIL: Patient not found.")


# TEST 3: Search for a report
print("\nTEST 3 - GET REPORT")
print("-------------------")

report = get_report_by_number(
    "MR999999"
)

if report:
    print("Report found:")
    print(report)

else:
    print("PASS: Non-existing report returned None.")