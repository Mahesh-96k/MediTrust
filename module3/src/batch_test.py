import pandas as pd
import joblib


MODEL_FILE = "models/isolation_forest.pkl"
SCALER_FILE = "models/scaler.pkl"

DATA_FILE = "data/medical_reports.csv"
OUTPUT_FILE = "data/batch_results.csv"


FEATURES = [
    "age",
    "hemoglobin",
    "glucose",
    "systolic_bp",
    "diastolic_bp",
    "heart_rate"
]


# Load dataset
df = pd.read_csv(DATA_FILE)

print("Total reports:", len(df))


# Load trained model
model = joblib.load(MODEL_FILE)
scaler = joblib.load(SCALER_FILE)


# Prepare data
X = df[FEATURES]

X_scaled = scaler.transform(X)


# Predict anomalies
predictions = model.predict(X_scaled)

scores = model.decision_function(X_scaled)


# Add results
df["ai_anomaly"] = predictions == -1
df["anomaly_score"] = scores


# Create readable status
df["status"] = df["ai_anomaly"].apply(
    lambda x: "ANOMALY" if x else "NORMAL"
)


# Save results
df.to_csv(OUTPUT_FILE, index=False)


# Display summary
print("\n================================")
print("BATCH ANOMALY DETECTION")
print("================================")

print(
    "Normal reports:",
    (df["status"] == "NORMAL").sum()
)

print(
    "Anomalous reports:",
    (df["status"] == "ANOMALY").sum()
)


print("\nTop 10 suspicious reports:")

suspicious = df.sort_values(
    "anomaly_score"
).head(10)

print(
    suspicious[
        [
            "report_id",
            "age",
            "hemoglobin",
            "glucose",
            "systolic_bp",
            "diastolic_bp",
            "heart_rate",
            "anomaly_score",
            "status"
        ]
    ].to_string(index=False)
)


print("\nResults saved to:")
print(OUTPUT_FILE)

