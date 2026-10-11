import subprocess
import sys


TESTS = [
    "test_medical_report.py",
    "test_field_validator.py",
    "test_patient_validator.py",
    "test_date_validator.py",
    "test_test_validator.py",
    "test_duplicate_detector.py",
    "test_similarity_detector.py",
    "test_fraud_engine.py",
    "test_clean_report.py",
    "test_multiple_indicators.py",
    "test_database.py",
    "test_repository.py",
    "test_save_report.py",
    "test_database_fraud_integration.py",
    "test_report_exists.py",
    "test_database_duplicate_engine.py",
    "test_new_report_database_engine.py",
    "test_get_all_reports.py",
    "test_database_similarity.py",
    "test_full_database_fraud_engine.py",
    "test_database_workflow.py",
    "test_multiple_database_indicators.py",
    "test_api.py",
    "test_member1_member2_integration.py",
    "test_suspicious_ocr_integration.py",
    "test_member2_output_contract.py"
]


print("========================================")
print("MEDTRUST MEMBER 2 TEST SUITE")
print("========================================")


passed = 0
failed = 0


for test in TESTS:

    print("\n----------------------------------------")
    print(f"RUNNING: {test}")
    print("----------------------------------------")

    result = subprocess.run(
        [sys.executable, test]
    )

    if result.returncode == 0:
        print(f"PASS: {test}")
        passed += 1
    else:
        print(f"FAIL: {test}")
        failed += 1


print("\n========================================")
print("MEMBER 2 TEST SUMMARY")
print("========================================")

print("Passed:", passed)
print("Failed:", failed)
print("Total :", len(TESTS))


if failed == 0:
    print("\nALL MEMBER 2 TESTS PASSED.")
else:
    print("\nSOME MEMBER 2 TESTS FAILED.")