# MediTrust - Medical Report Validation & Fraud Detection Engine

## Module

Member 2 - Medical Report Validation & Fraud Detection Engine

## Purpose

This module performs automated preliminary validation and fraud-related
screening on structured medical report data received after OCR/document
processing.

The module checks medical reports for missing information, invalid patient
identifiers, patient information inconsistencies, invalid dates, abnormal
laboratory values, duplicate reports, and highly similar reports.

The output contains validation/fraud indicators with category, severity,
and explanation.

This is a preliminary screening system and does not prove that a medical
report is fraudulent.

---

## Main Responsibilities

- Validate required medical report fields
- Validate patient ID format
- Compare patient information with stored database records
- Validate report dates
- Validate laboratory test values
- Check laboratory reference ranges
- Detect duplicate report numbers
- Detect highly similar reports
- Assign indicator categories
- Assign indicator severity
- Return structured analysis results
- Provide a Flask API for integration with the OCR module

---

## Project Structure

```text
fraud_engine/
│
├── app.py
├── analysis_result.py
├── database.py
├── fraud_engine.py
├── indicator_categories.py
├── indicator_formatter.py
├── indicator_severity.py
├── medical_report.py
├── repository.py
├── requirements.txt
├── README.md
│
├── validation/
│   ├── __init__.py
│   ├── field_validator.py
│   ├── patient_validator.py
│   ├── date_validator.py
│   └── test_validator.py
│
├── duplicate/
│   ├── __init__.py
│   ├── duplicate_detector.py
│   ├── similarity_detector.py
│   ├── database_duplicate_detector.py
│   └── database_similarity_detector.py
│
├── sample_ocr_output.json
├── sample_ocr_suspicious.json
└── run_member2_tests.py