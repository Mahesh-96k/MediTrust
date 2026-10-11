# ============================================================
# RISK CLASSIFICATION
# ============================================================

def classify_risk(score):

    if score <= 2:
        return "LOW"

    elif score <= 5:
        return "MEDIUM"

    else:
        return "HIGH"


def get_verification_status(risk_level):

    if risk_level == "LOW":

        return "No immediate suspicious indicators detected."

    elif risk_level == "MEDIUM":

        return "Manual verification recommended."

    else:

        return "Further verification required."
