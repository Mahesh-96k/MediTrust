import os
import joblib
import pandas as pd

from risk_scoring import calculate_risk_score
from risk_classifier import (
    classify_risk,
    get_verification_status
)


# ============================================================
# PATH CONFIGURATION
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

MODEL_FILE = os.path.join(
    BASE_DIR,
    "models",
    "isolation_forest.pkl"
)

SCALER_FILE = os.path.join(
    BASE_DIR,
    "models",
    "scaler.pkl"
)


# ============================================================
# LOAD TRAINED MODEL AND SCALER
# ============================================================

model = joblib.load(MODEL_FILE)

scaler = joblib.load(SCALER_FILE)


# ============================================================
# FEATURES USED BY THE AI MODEL
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
# AI ANOMALY DETECTION
# ============================================================

def detect_anomaly(medical_data):

    # Convert medical data into a DataFrame
    data = pd.DataFrame(
        [medical_data],
        columns=FEATURES
    )

    # Scale the data
    scaled_data = scaler.transform(data)

    # Get Isolation Forest prediction
    prediction = model.predict(
        scaled_data
    )[0]

    # Get anomaly score
    anomaly_score = model.decision_function(
        scaled_data
    )[0]

    # Isolation Forest:
    # -1 = anomaly
    #  1 = normal

    is_anomaly = prediction == -1

    return (
        bool(is_anomaly),
        float(anomaly_score)
    )


# ============================================================
# COMPLETE REPORT ANALYSIS
# ============================================================

def analyze_report(
    medical_data,
    validation_indicators
):

    # --------------------------------------------------------
    # STEP 1: AI ANOMALY DETECTION
    # --------------------------------------------------------

    is_anomaly, anomaly_score = detect_anomaly(
        medical_data
    )


    # --------------------------------------------------------
    # STEP 2: COPY VALIDATION INDICATORS
    # --------------------------------------------------------

    indicators = dict(
        validation_indicators
    )


    # --------------------------------------------------------
    # STEP 3: ADD AI ANOMALY TO INDICATORS
    # --------------------------------------------------------

    indicators["ai_anomaly"] = bool(
        is_anomaly
    )


    # --------------------------------------------------------
    # STEP 4: CALCULATE RISK SCORE
    # --------------------------------------------------------

    risk_score, reasons = calculate_risk_score(
        indicators
    )


    # --------------------------------------------------------
    # STEP 5: CLASSIFY RISK
    # --------------------------------------------------------

    risk_level = classify_risk(
        risk_score
    )


    # --------------------------------------------------------
    # STEP 6: GET VERIFICATION STATUS
    # --------------------------------------------------------

    verification_status = get_verification_status(
        risk_level
    )


    # --------------------------------------------------------
    # STEP 7: CREATE JSON-SAFE REASONS
    # --------------------------------------------------------

    safe_reasons = []

    for reason in reasons:

        safe_reasons.append({

            "indicator": str(
                reason["indicator"]
            ),

            "points": int(
                reason["points"]
            ),

            "message": str(
                reason["message"]
            )
        })


    # --------------------------------------------------------
    # STEP 8: ALWAYS PROVIDE A REASON
    # --------------------------------------------------------

    if len(safe_reasons) == 0:

        safe_reasons.append({

            "indicator":
                "no_suspicious_indicators",

            "points": 0,

            "message":
                "No suspicious indicators were detected "
                "by the current AI and validation checks."
        })


    # --------------------------------------------------------
    # STEP 9: CREATE FINAL RESULT
    # --------------------------------------------------------

    result = {

        "ai_anomaly": bool(
            is_anomaly
        ),

        "anomaly_score": float(
            round(anomaly_score, 4)
        ),

        "risk_score": int(
            risk_score
        ),

        "risk_level": str(
            risk_level
        ),

        "verification_status": str(
            verification_status
        ),

        "reasons": safe_reasons
    }


    return result


# ============================================================
# DIRECT TEST
# ============================================================

if __name__ == "__main__":

    # --------------------------------------------------------
    # TEST MEDICAL DATA
    # --------------------------------------------------------

    test_medical_data = {

        "age": 25,

        "hemoglobin": 13.5,

        "glucose": 98,

        "systolic_bp": 120,

        "diastolic_bp": 80,

        "heart_rate": 75
    }


    # --------------------------------------------------------
    # TEST VALIDATION INDICATORS
    # --------------------------------------------------------

    test_validation_indicators = {

        "patient_id_inconsistency": False,

        "duplicate_report": False,

        "invalid_date": False,

        "missing_field": False,

        "lab_inconsistency": False,

        "information_inconsistency": False
    }


    # --------------------------------------------------------
    # ANALYZE TEST REPORT
    # --------------------------------------------------------

    result = analyze_report(

        test_medical_data,

        test_validation_indicators
    )


    # --------------------------------------------------------
    # DISPLAY RESULT
    # --------------------------------------------------------

    print()
    print("===================================")
    print("       MODULE 3 RISK RESULT")
    print("===================================")

    print(
        "AI Anomaly       :",
        result["ai_anomaly"]
    )

    print(
        "Anomaly Score    :",
        result["anomaly_score"]
    )

    print(
        "Risk Score       :",
        result["risk_score"]
    )

    print(
        "Risk Level       :",
        result["risk_level"]
    )

    print(
        "Verification     :",
        result["verification_status"]
    )

    print()
    print("Reasons:")

    for reason in result["reasons"]:

        print(
            "-",
            reason["message"],
            "(Points:",
            reason["points"],
            ")"
        )

    print("===================================")
