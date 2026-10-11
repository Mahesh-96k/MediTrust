import pandas as pd
import numpy as np

# Make results reproducible
np.random.seed(42)

# -----------------------------
# 1. Generate normal reports
# -----------------------------

normal_count = 500

normal_data = {
    "age": np.random.randint(18, 70, normal_count),

    "hemoglobin": np.random.normal(13.5, 1.2, normal_count),

    "glucose": np.random.normal(100, 15, normal_count),

    "systolic_bp": np.random.normal(120, 10, normal_count),

    "diastolic_bp": np.random.normal(80, 7, normal_count),

    "heart_rate": np.random.normal(75, 8, normal_count)
}

normal_df = pd.DataFrame(normal_data)

# -----------------------------
# 2. Generate anomalous reports
# -----------------------------

anomaly_count = 30

anomaly_data = {
    "age": np.random.randint(18, 70, anomaly_count),

    "hemoglobin": np.random.uniform(2, 6, anomaly_count),

    "glucose": np.random.uniform(250, 700, anomaly_count),

    "systolic_bp": np.random.uniform(180, 280, anomaly_count),

    "diastolic_bp": np.random.uniform(120, 190, anomaly_count),

    "heart_rate": np.random.uniform(120, 180, anomaly_count)
}

anomaly_df = pd.DataFrame(anomaly_data)

# -----------------------------
# 3. Combine datasets
# -----------------------------

df = pd.concat(
    [normal_df, anomaly_df],
    ignore_index=True
)

# Shuffle the rows
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Round medical values
df["hemoglobin"] = df["hemoglobin"].round(2)
df["glucose"] = df["glucose"].round(2)
df["systolic_bp"] = df["systolic_bp"].round(2)
df["diastolic_bp"] = df["diastolic_bp"].round(2)
df["heart_rate"] = df["heart_rate"].round(2)

# Add synthetic report ID
df.insert(
    0,
    "report_id",
    ["RPT" + str(i).zfill(4) for i in range(1, len(df) + 1)]
)

# Save dataset
output_file = "data/medical_reports.csv"

df.to_csv(output_file, index=False)

print("Dataset created successfully!")
print(f"Total reports: {len(df)}")
print(f"Saved to: {output_file}")

print("\nFirst 10 records:")
print(df.head(10))

print("\nDataset statistics:")
print(df.describe())
