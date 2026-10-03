from repository import get_all_medical_reports


print("GET ALL MEDICAL REPORTS TEST")
print("============================")

reports = get_all_medical_reports()

print("\nTOTAL REPORTS")
print("-------------")
print(len(reports))

print("\nREPORTS")
print("-------")

for report in reports:
    print(
        report.report_number,
        "|",
        report.patient_id,
        "|",
        report.patient_name,
        "|",
        report.report_date
    )

    for test in report.tests:
        print(
            "   TEST:",
            test.name,
            "| VALUE:",
            test.value,
            "| RANGE:",
            test.reference_min,
            "-",
            test.reference_max
        )