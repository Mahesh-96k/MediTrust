import json
import requests


BASE_URL = "http://127.0.0.1:5000"


print("SUSPICIOUS OCR → MEMBER 2 TEST")
print("===============================")


with open(
    "sample_ocr_suspicious.json",
    "r",
    encoding="utf-8"
) as file:
    report = json.load(file)


print("\nOCR OUTPUT LOADED")
print("-----------------")
print("Report Number:", report["report_number"])
print("Patient ID:", report["patient_id"])
print("Patient Name:", report["patient_name"])
print("Report Date:", report["report_date"])


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

    print(
        "   Reason:",
        indicator["reason"]
    )


print("\n===============================")
print("SUSPICIOUS OCR TEST COMPLETED")
print("===============================")