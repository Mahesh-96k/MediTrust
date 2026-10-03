import requests


BASE_URL = "http://127.0.0.1:5000"


print("MEDTRUST FLASK API TEST")
print("=======================")


# --------------------------------------------------
# TEST 1 - HOME
# --------------------------------------------------

print("\nTEST 1 - HOME")
print("-------------")

response = requests.get(
    f"{BASE_URL}/"
)

print("Status:", response.status_code)
print("Response:", response.json())


# --------------------------------------------------
# TEST 2 - HEALTH
# --------------------------------------------------

print("\nTEST 2 - HEALTH")
print("---------------")

response = requests.get(
    f"{BASE_URL}/health"
)

print("Status:", response.status_code)
print("Response:", response.json())


# --------------------------------------------------
# TEST 3 - VALID MEDICAL REPORT
# --------------------------------------------------

print("\nTEST 3 - VALID REPORT")
print("---------------------")

report = {
    "report_number": "MR8001",
    "patient_id": "P50001",
    "patient_name": "Anita Sharma",
    "report_date": "2026-09-25",
    "doctor": "Dr. Mehta",
    "hospital": "City Hospital",
    "diagnosis": "Routine Checkup",
    "tests": [
        {
            "name": "Glucose",
            "value": 100.0,
            "reference_min": 70.0,
            "reference_max": 140.0,
            "unit": "mg/dL"
        },
        {
            "name": "Hemoglobin",
            "value": 13.5,
            "reference_min": 12.0,
            "reference_max": 16.0,
            "unit": "g/dL"
        }
    ]
}

response = requests.post(
    f"{BASE_URL}/analyze",
    json=report
)

print("Status:", response.status_code)
print("Response:")

print(response.json())


# --------------------------------------------------
# TEST 4 - MISSING API FIELDS
# --------------------------------------------------

print("\nTEST 4 - MISSING FIELDS")
print("-----------------------")

invalid_report = {
    "report_number": "MR9001",
    "patient_id": "P50001"
}

response = requests.post(
    f"{BASE_URL}/analyze",
    json=invalid_report
)

print("Status:", response.status_code)
print("Response:")

print(response.json())


print("\n=======================")
print("API TESTS COMPLETED")
print("=======================")