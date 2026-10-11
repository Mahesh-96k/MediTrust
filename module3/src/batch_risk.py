import pandas as pd
import joblib

from risk_scoring import calculate_risk_score
from risk_classifier import classify_risk


MODEL_FILE = "models/isolation_forest.pkl"
SCALER_FILE = "models/scaler.pkl"

INPUT_FILE = "data/medical_reports.csv"
OUTPUT_FILE = "data/final_risk_results.csv"


FEATURES = [
    "age",
    "hemoglobin",
    "glucose",
    "systolic_bp",
    "diastolic_bp",
    "heart_rate"
]


# Load dataset
df = pd.read_csv(INPUT_FILE)

print("Total reports:", len(df))


# Load trained AI model
model = joblib.load(MODEL_FILE)
scaler = joblib.load(SCALER_FILE)


# Prepare medical data
X = df[FEATURES]

X_scaled = scaler.transform(X)


# AI anomaly detection
predictions = model.predict(X_scaled)

scores = model.decision_function(X_scaled)

df["ai_anomaly"] = predictions == -1

df["anomaly_score"] = scores


# Lists for final results
risk_scores = []
risk_levels = []
risk_reasons = []


# Analyze every report
for _, row in df.iterrows():

    indicators = {
        "ai_anomaly": bool(row["ai_anomaly"]),

        "patient_id_inconsistency": False,

        "duplicate_report": False,

        "invalid_date": False,

        "missing_field": False,

        "lab_inconsistency": False,

        "information_inconsistency": False
    }


    # Temporary simulation of Module 2 results
    # These will later come from the real Module 2.

    report_number = int(
        row["report_id"].replace("RPT", "")
    )


    if report_number % 17 == 0:
        indicators["patient_id_inconsistency"] = True


    if report_number % 23 == 0:
        indicators["duplicate_report"] = True


    if report_number % 29 == 0:
        indicators["invalid_date"] = True


    if report_number % 31 == 0:
        indicators["missing_field"] = True


    if report_number % 37 == 0:
        indicators["lab_inconsistency"] = True


    # Calculate risk score
    score, reasons = calculate_risk_score(
        indicators
    )


    # Calculate risk level
    level = classify_risk(score)


    # Store results
    risk_scores.append(score)

    risk_levels.append(level)


    reason_text = ", ".join(
        reason["indicator"]
        for reason in reasons
    )

    risk_reasons.append(reason_text)


# Add results to dataframe
df["risk_score"] = risk_scores

df["risk_level"] = risk_levels

df["risk_reasons"] = risk_reasons


# Save final results
df.to_csv(
    OUTPUT_FILE,
    index=False
)


# Display summary
print("\n================================")
print("AI RISK INTELLIGENCE")
print("================================")

print(
    "LOW:",
    (df["risk_level"] == "LOW").sum()
)

print(
    "MEDIUM:",
    (df["risk_level"] == "MEDIUM").sum()
)

print(
    "HIGH:",
    (df["risk_level"] == "HIGH").sum()
)


print("\nHighest risk reports:")

highest_risk = df.sort_values(
    "risk_score",
    ascending=False
).head(10)


print(
    highest_risk[
        [
            "report_id",
            "ai_anomaly",
            "anomaly_score",
            "risk_score",
            "risk_level",
            "risk_reasons"
        ]
    ].to_string(index=False)
)


print("\nFinal results saved to:")

print(OUTPUT_FILE)
