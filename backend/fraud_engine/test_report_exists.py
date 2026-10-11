from repository import report_exists


print("DATABASE DUPLICATE CHECK")
print("========================")


# Existing report
print("\nTEST 1 - EXISTING REPORT")
print("------------------------")

result = report_exists("MR5001")

if result:
    print("PASS: MR5001 exists in the database.")
else:
    print("FAIL: MR5001 was not found.")


# Non-existing report
print("\nTEST 2 - NEW REPORT")
print("-------------------")

result = report_exists("MR9999")

if not result:
    print("PASS: MR9999 does not exist.")
else:
    print("FAIL: MR9999 was incorrectly detected.")