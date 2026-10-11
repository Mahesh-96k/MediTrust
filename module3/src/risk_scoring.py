# ============================================================
# RISK SCORING
# ============================================================

RISK_WEIGHTS = {
    "ai_anomaly": 2,
    "patient_id_inconsistency": 3,
    "duplicate_report": 3,
    "invalid_date": 2,
    "missing_field": 1,
    "lab_inconsistency": 2,
    "information_inconsistency": 2
}


RISK_MESSAGES = {
    "ai_anomaly":
        "AI model detected an unusual pattern in the medical data.",

    "patient_id_inconsistency":
        "Patient information is inconsistent with the report data.",

    "duplicate_report":
        "A possible duplicate medical report was detected.",

    "invalid_date":
        "The report contains an invalid or suspicious date.",

    "missing_field":
        "One or more required report fields are missing.",

    "lab_inconsistency":
        "The laboratory information contains an inconsistency.",

    "information_inconsistency":
        "Different parts of the report contain inconsistent information."
}


def calculate_risk_score(indicators):

    score = 0
    reasons = []

    for indicator, detected in indicators.items():

        if detected:

            points = RISK_WEIGHTS.get(
                indicator,
                0
            )

            message = RISK_MESSAGES.get(
                indicator,
                "A suspicious indicator was detected."
            )

            score += points

            reasons.append({
                "indicator": indicator,
                "points": points,
                "message": message
            })

    return score, reasons
