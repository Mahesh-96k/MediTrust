from medical_report import MedicalReport, TestResult
from validation.field_validator import validate_required_fields

invalid_report = MedicalReport(
    report_number="MR1002",
    patient_id="",
    patient_name="Rahul Kumar",
    report_date="2026-09-20",
    doctor="Dr. Sharma",
    hospital="ABC Hospital",
    diagnosis="Diabetes",
    tests=[]
)


indicators = validate_required_fields(invalid_report)

print("INVALID REPORT TEST")
print("-------------------")

for indicator in indicators:
    print(indicator)