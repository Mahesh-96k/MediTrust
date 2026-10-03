import requests


BASE_URL = "http://127.0.0.1:5000"


report = {
    "report_number": "MR9001",
    "patient_id": "P50001",
    "patient_name": "Anita Sharma",
    "report_date": "2026-09-25",
    "doctor": "Dr. Mehta",
    "hospital": "City Hospital",
    "diagnosis": "Routine Checkup",
    "tests": [
        {
            "name": "Glucose",
            "value": 500.0,
            "reference_min": 70.0,
            "reference_max": 140.0,
            "unit": "mg/dL"
        }
    ]
}


print("MEMBER 2 OUTPUT CONTRACT TEST")
print("=============================")

response = requests.post(
    f"{BASE_URL}/analyze",
    json=report
)

print("\nHTTP STATUS")
print("-----------")
print(response.status_code)

result = response.json()

print("\nRESPONSE")
print("--------")
print(result)


# --------------------------------------------------
# Check top-level fields
# --------------------------------------------------

required_top_level_fields = [
    "success",
    "total_indicators",
    "has_issues",
    "summary",
    "indicators"
]

print("\nTOP-LEVEL CONTRACT")
print("------------------")

for field in required_top_level_fields:

    if field in result:
        print(f"PASS: {field}")
    else:
        print(f"FAIL: {field}")


# --------------------------------------------------
# Check indicator fields
# --------------------------------------------------

print("\nINDICATOR CONTRACT")
print("------------------")

required_indicator_fields = [
    "type",
    "category",
    "severity",
    "reason"
]

indicators = result.get("indicators", [])

if not indicators:
    print("FAIL: No indicators returned.")
else:

    for index, indicator in enumerate(indicators):

        print(f"\nIndicator {index + 1}")

        for field in required_indicator_fields:

            if field in indicator:
                print(
                    f"PASS: {field} = "
                    f"{indicator[field]}"
                )
            else:
                print(
                    f"FAIL: {field} is missing"
                )


print("\n=============================")
print("OUTPUT CONTRACT TEST COMPLETE")
print("=============================")