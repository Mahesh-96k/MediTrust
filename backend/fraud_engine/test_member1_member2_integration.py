import json
import requests


BASE_URL = "http://127.0.0.1:5000"

print("MEMBER 1 → MEMBER 2 INTEGRATION TEST")
print("=====================================")


# Load OCR-style structured output
with open(
    "sample_ocr_output.json",
    "r",
    encoding="utf-8"
) as file:
    report = json.load(file)


print("\nOCR OUTPUT LOADED")
print("-----------------")
print("Report Number:", report["report_number"])
print("Patient ID:", report["patient_id"])
print("Patient Name:", report["patient_name"])


# Send OCR output to Member 2 API
response = requests.post(
    f"{BASE_URL}/analyze",
    json=report
)


print("\nAPI RESPONSE")
print("------------")
print("Status:", response.status_code)

result = response.json()

print("Success:", result.get("success"))
print(
    "Total Indicators:",
    result.get("total_indicators")
)
print(
    "Has Issues:",
    result.get("has_issues")
)
print(
    "Summary:",
    result.get("summary")
)


print("\nINDICATORS")
print("----------")

for indicator in result.get("indicators", []):
    print(
        indicator["type"],
        "|",
        indicator["category"],
        "|",
        indicator["severity"]
    )

print("\n=====================================")
print("MEMBER 1 → MEMBER 2 TEST COMPLETED")
print("=====================================")