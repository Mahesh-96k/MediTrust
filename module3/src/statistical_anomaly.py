import os
import joblib
import pandas as pd
import numpy as np


# ============================================================
# PATH CONFIGURATION
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

DATA_FILE = os.path.join(
    BASE_DIR,
    "data",
    "medical_reports.csv"
)


# ============================================================
# FEATURES
# ============================================================

FEATURES = [
    "age",
    "hemoglobin",
    "glucose",
    "systolic_bp",
    "diastolic_bp",
    "heart_rate"
]


# ============================================================
# LOAD DATASET
# ============================================================

df = pd.read_csv(DATA_FILE)


# ============================================================
# CALCULATE STATISTICAL PARAMETERS
# ============================================================

MEANS = df[FEATURES].mean()

STDS = df[FEATURES].std()


# ============================================================
# STATISTICAL ANOMALY DETECTION
# ============================================================

def detect_statistical_anomaly(
    medical_data,
    threshold=3.0
):

    values = pd.Series(
        medical_data
    )

    z_scores = {}

    suspicious_features = []

    for feature in FEATURES:

        value = float(
            values[feature]
        )

        mean = float(
            MEANS[feature]
        )

        std = float(
            STDS[feature]
        )

        if std == 0:

            z_score = 0.0

        else:

            z_score = (
                (value - mean) / std
            )

        z_scores[feature] = round(
            float(z_score),
            4
        )

        if abs(z_score) >= threshold:

            suspicious_features.append(
                feature
            )


    # Maximum absolute z-score
    max_z_score = max(
        abs(value)
        for value in z_scores.values()
    )


    # Determine anomaly
    is_anomaly = (
        len(suspicious_features) > 0
    )


    return {
        "is_anomaly": bool(
            is_anomaly
        ),

        "max_z_score": float(
            round(max_z_score, 4)
        ),

        "z_scores": z_scores,

        "suspicious_features":
            suspicious_features
    }


# ============================================================
# DIRECT TEST
# ============================================================

if __name__ == "__main__":

    test_data = {

        "age": 45,

        "hemoglobin": 3.5,

        "glucose": 600,

        "systolic_bp": 250,

        "diastolic_bp": 160,

        "heart_rate": 160
    }


    result = detect_statistical_anomaly(
        test_data
    )


    print()
    print("======================================")
    print(" STATISTICAL ANOMALY TEST")
    print("======================================")

    print(
        "Anomaly:",
        result["is_anomaly"]
    )

    print(
        "Maximum Z-Score:",
        result["max_z_score"]
    )

    print(
        "Suspicious Features:",
        result["suspicious_features"]
    )

    print()
    print("Z-Scores:")

    for feature, score in result[
        "z_scores"
    ].items():

        print(
            f"  {feature}: {score}"
        )

    print("======================================")
