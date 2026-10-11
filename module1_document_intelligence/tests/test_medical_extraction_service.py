from app.services.medical_extraction_service import (
    extract_blood_pressure,
    extract_date,
    extract_diagnoses,
    extract_patient_age,
    extract_doctor_name,
    extract_hospital_name,
    extract_medical_information,
    extract_patient_name,
    extract_temperature,
)


def test_extract_patient_name():
    text = "Patient Name: John Smith"

    assert extract_patient_name(text) == "John Smith"

def test_extract_full_patient_name():
    text = "Full name of patient: Mr Tan Ah Kow"

    assert extract_patient_name(text) == "Mr Tan Ah Kow"

def test_extract_doctor_name():
    text = "Full name of doctor: Tan Ah Moi"

    assert extract_doctor_name(text) == "Tan Ah Moi"

def test_extract_date():
    text = "Date: 04/10/2026"

    assert extract_date(text) == "04/10/2026"


def test_extract_blood_pressure():
    text = "Blood Pressure: 120/80"

    assert extract_blood_pressure(text) == "120/80"


def test_extract_temperature():
    text = "Temperature: 98.6 F"

    assert extract_temperature(text) == "98.6 F"

def test_extract_patient_age():
    text = "Age of patient: 55 years old"

    result = extract_patient_age(text)

    assert result == "55"

def test_extract_medical_information():
    text = """
    Patient Name: John Smith
    Full name of doctor: Tan Ah Moi
    Age of patient: 55 years old
    Hospital / Clinic name and address: 1 Blackacre Hospital, Singapore 01010101
    Date: 04/10/2026
    Blood Pressure: 120/80
    Temperature: 98.6 F
    Diagnosis:
    1. Dementia
    2. Stroke
    """

    result = extract_medical_information(text)

    assert result == {
        "patient_name": "John Smith",
        "patient_age": "55",
        "doctor_name": "Tan Ah Moi",
        "hospital_name": "1 Blackacre Hospital, Singapore 01010101",
        "date": "04/10/2026",
        "blood_pressure": "120/80",
        "temperature": "98.6 F",
        "diagnoses": ["Dementia", "Stroke"],
    }

def test_extract_hospital_name():
    text = (
        "Hospital / Clinic name and address: "
        "1 Blackacre Hospital, Singapore 01010101"
    )

    assert (
        extract_hospital_name(text)
        == "1 Blackacre Hospital, Singapore 01010101"
    )

def test_extract_diagnoses():
    text = """
    Diagnosis:
    1. Dementia
    2. Stroke
    """

    assert extract_diagnoses(text) == [
        "Dementia",
        "Stroke",
    ]

def test_missing_information_returns_none():
    text = "Medical Report"

    result = extract_medical_information(text)

    assert result == {
        "patient_name": None,
        "doctor_name": None,
        "hospital_name": None,
        "patient_age":None,
        "date": None,
        "blood_pressure": None,
        "temperature": None,
        "diagnoses": [],
    }