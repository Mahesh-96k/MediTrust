import json
import urllib.request


API_URL = "http://127.0.0.1:5000/analyze"


report = {
    "report_id": "RPT3001",

    "medical_data": {
        "age": 35,
        "hemoglobin": 13.8,
        "glucose": 102,
        "systolic_bp": 118,
        "diastolic_bp": 79,
        "heart_rate": 76
    },

    "validation_indicators": {
        "patient_id_inconsistency": False,
        "duplicate_report": False,
        "invalid_date": False,
        "missing_field": False,
        "lab_inconsistency": False,
        "information_inconsistency": False
    }
}


# Convert report to JSON
request_data = json.dumps(report).encode("utf-8")


# Create POST request
request = urllib.request.Request(
    API_URL,
    data=request_data,
    headers={
        "Content-Type": "application/json"
    },
    method="POST"
)


# Send request
with urllib.request.urlopen(request) as response:

    result = json.loads(
        response.read().decode("utf-8")
    )


# Print result
print("\n===== API RESULT =====")

print(
    json.dumps(
        result,
        indent=4
    )
)


# Save result
output_file = (
    "data/api_results/RPT3001_result.json"
)

with open(
    output_file,
    "w"
) as file:

    json.dump(
        result,
        file,
        indent=4
    )


print("\nResult saved to:")
print(output_file)
