from risk_scoring import calculate_risk_score
from risk_classifier import classify_risk


# Example indicators received from Module 2
indicators = {
    "ai_anomaly": False,
    "patient_id_inconsistency": False,
    "duplicate_report": False,
    "invalid_date": False,
    "missing_field": True,
    "lab_inconsistency": False,
    "information_inconsistency": False
}


# Calculate score
score, reasons = calculate_risk_score(indicators)

# Classify risk
risk_level = classify_risk(score)


print("--------------------------------")
print("MEDICAL REPORT RISK ANALYSIS")
print("--------------------------------")

print("Risk Score:", score)
print("Risk Level:", risk_level)

print("\nDetected Indicators:")

for reason in reasons:
    print(
        f"- {reason['indicator']} "
        f"(+{reason['points']})"
    )
