import pandas as pd
import joblib

from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler


# -----------------------------------
# 1. Load the medical report dataset
# -----------------------------------

DATA_FILE = "data/medical_reports.csv"
MODEL_FILE = "models/isolation_forest.pkl"
SCALER_FILE = "models/scaler.pkl"
OUTPUT_FILE = "data/anomaly_results.csv"

df = pd.read_csv(DATA_FILE)

print("Dataset loaded successfully.")
print("Total reports:", len(df))


# -----------------------------------
# 2. Select medical features
# -----------------------------------

features = [
    "age",
    "hemoglobin",
    "glucose",
    "systolic_bp",
    "diastolic_bp",
    "heart_rate"
]

X = df[features]


# -----------------------------------
# 3. Scale the data
# -----------------------------------

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)


# -----------------------------------
# 4. Create Isolation Forest model
# -----------------------------------

model = IsolationForest(
    n_estimators=200,
    contamination=0.06,
    random_state=42
)


# -----------------------------------
# 5. Train the model
# -----------------------------------

model.fit(X_scaled)


# -----------------------------------
# 6. Predict anomalies
# -----------------------------------

predictions = model.predict(X_scaled)

scores = model.decision_function(X_scaled)


# -----------------------------------
# 7. Convert prediction to readable form
# -----------------------------------

df["anomaly_prediction"] = predictions
df["anomaly_score"] = scores

df["anomaly_status"] = df["anomaly_prediction"].apply(
    lambda x: "ANOMALY" if x == -1 else "NORMAL"
)


# -----------------------------------
# 8. Save model and scaler
# -----------------------------------

joblib.dump(model, MODEL_FILE)
joblib.dump(scaler, SCALER_FILE)


# -----------------------------------
# 9. Save results
# -----------------------------------

df.to_csv(OUTPUT_FILE, index=False)


# -----------------------------------
# 10. Display results
# -----------------------------------

print("\nAnomaly detection completed.")

print("\nNormal reports:")
print((df["anomaly_status"] == "NORMAL").sum())

print("\nAnomalous reports:")
print((df["anomaly_status"] == "ANOMALY").sum())

print("\nSample results:")
print(
    df[
        [
            "report_id",
            "anomaly_score",
            "anomaly_status"
        ]
    ].head(20)
)

print("\nModel saved to:", MODEL_FILE)
print("Results saved to:", OUTPUT_FILE)
