from typing import List, Optional

from medical_report import MedicalReport, TestResult
from database import create_connection


def get_patient(patient_id: str) -> Optional[dict]:
    """
    Retrieve a patient from MySQL using patient ID.
    """

    connection = create_connection()

    if connection is None:
        return None

    cursor = connection.cursor(dictionary=True)

    try:
        query = """
            SELECT patient_id, patient_name
            FROM patients
            WHERE patient_id = %s
        """

        cursor.execute(query, (patient_id,))

        return cursor.fetchone()

    finally:
        cursor.close()
        connection.close()


def insert_patient(
    patient_id: str,
    patient_name: str
) -> bool:
    """
    Insert a patient into MySQL.
    """

    connection = create_connection()

    if connection is None:
        return False

    cursor = connection.cursor()

    try:
        query = """
            INSERT INTO patients (
                patient_id,
                patient_name
            )
            VALUES (%s, %s)
        """

        cursor.execute(
            query,
            (patient_id, patient_name)
        )

        connection.commit()

        return True

    except Exception as error:
        connection.rollback()
        print("Patient insertion failed:", error)
        return False

    finally:
        cursor.close()
        connection.close()


def get_report_by_number(
    report_number: str
) -> Optional[MedicalReport]:
    """
    Retrieve a medical report using report number.
    """

    connection = create_connection()

    if connection is None:
        return None

    cursor = connection.cursor(dictionary=True)

    try:
        query = """
            SELECT
                report_number,
                patient_id,
                patient_name,
                DATE_FORMAT(report_date, '%Y-%m-%d')
                    AS report_date,
                doctor,
                hospital,
                diagnosis
            FROM medical_reports
            WHERE report_number = %s
        """

        cursor.execute(
            query,
            (report_number,)
        )

        row = cursor.fetchone()

        if row is None:
            return None

        tests = get_tests_for_report(
            row["report_number"]
        )

        return MedicalReport(
            report_number=row["report_number"],
            patient_id=row["patient_id"],
            patient_name=row["patient_name"],
            report_date=row["report_date"],
            doctor=row["doctor"],
            hospital=row["hospital"],
            diagnosis=row["diagnosis"],
            tests=tests
        )

    finally:
        cursor.close()
        connection.close()


def get_tests_for_report(
    report_number: str
) -> List[TestResult]:
    """
    Retrieve laboratory test results for a report.
    """

    connection = create_connection()

    if connection is None:
        return []

    cursor = connection.cursor(dictionary=True)

    try:
        query = """
            SELECT
                tr.test_name,
                tr.test_value,
                tr.reference_min,
                tr.reference_max,
                tr.unit
            FROM test_results tr
            INNER JOIN medical_reports mr
                ON tr.report_id = mr.id
            WHERE mr.report_number = %s
        """

        cursor.execute(
            query,
            (report_number,)
        )

        rows = cursor.fetchall()

        return [
            TestResult(
                name=row["test_name"],
                value=float(row["test_value"]),
                reference_min=(
                    float(row["reference_min"])
                    if row["reference_min"] is not None
                    else None
                ),
                reference_max=(
                    float(row["reference_max"])
                    if row["reference_max"] is not None
                    else None
                ),
                unit=row["unit"]
            )
            for row in rows
        ]

    finally:
        cursor.close()
        connection.close()

def save_medical_report(report: MedicalReport) -> bool:
    """
    Save a complete medical report and its test results
    into MySQL.

    The patient is inserted if the patient does not
    already exist.
    """

    connection = create_connection()

    if connection is None:
        return False

    cursor = connection.cursor()

    try:
        # ------------------------------------------------
        # 1. Insert patient if the patient does not exist
        # ------------------------------------------------

        patient_query = """
            INSERT INTO patients (
                patient_id,
                patient_name
            )
            VALUES (%s, %s)
            ON DUPLICATE KEY UPDATE
                patient_name = VALUES(patient_name)
        """

        cursor.execute(
            patient_query,
            (
                report.patient_id,
                report.patient_name
            )
        )

        # ------------------------------------------------
        # 2. Insert medical report
        # ------------------------------------------------

        report_query = """
            INSERT INTO medical_reports (
                report_number,
                patient_id,
                patient_name,
                report_date,
                doctor,
                hospital,
                diagnosis
            )
            VALUES (
                %s, %s, %s, %s, %s, %s, %s
            )
        """

        cursor.execute(
            report_query,
            (
                report.report_number,
                report.patient_id,
                report.patient_name,
                report.report_date,
                report.doctor,
                report.hospital,
                report.diagnosis
            )
        )

        report_id = cursor.lastrowid

        # ------------------------------------------------
        # 3. Insert laboratory test results
        # ------------------------------------------------

        test_query = """
            INSERT INTO test_results (
                report_id,
                test_name,
                test_value,
                reference_min,
                reference_max,
                unit
            )
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        for test in report.tests:

            cursor.execute(
                test_query,
                (
                    report_id,
                    test.name,
                    test.value,
                    test.reference_min,
                    test.reference_max,
                    test.unit
                )
            )

        # ------------------------------------------------
        # 4. Save everything
        # ------------------------------------------------

        connection.commit()

        print(
            f"Medical report {report.report_number} "
            "saved successfully."
        )

        return True

    except Exception as error:

        connection.rollback()

        print(
            "Medical report insertion failed:",
            error
        )

        return False

    finally:

        cursor.close()
        connection.close()

def report_exists(report_number: str) -> bool:
    """
    Check whether a report number already exists
    in the medical_reports table.
    """

    connection = create_connection()

    if connection is None:
        return False

    cursor = connection.cursor()

    try:
        query = """
            SELECT id
            FROM medical_reports
            WHERE report_number = %s
            LIMIT 1
        """

        cursor.execute(
            query,
            (report_number,)
        )

        result = cursor.fetchone()

        return result is not None

    finally:
        cursor.close()
        connection.close()

def get_all_medical_reports() -> List[MedicalReport]:
    connection = create_connection()

    if connection is None:
        return []

    cursor = connection.cursor(dictionary=True)

    try:
        report_query = """
            SELECT
                mr.id,
                mr.report_number,
                mr.patient_id,
                mr.patient_name,
                DATE_FORMAT(
                    mr.report_date,
                    '%Y-%m-%d'
                ) AS report_date,
                mr.doctor,
                mr.hospital,
                mr.diagnosis
            FROM medical_reports mr
            ORDER BY mr.id
        """

        cursor.execute(report_query)
        report_rows = cursor.fetchall()

        reports = []

        for row in report_rows:

            test_query = """
                SELECT
                    test_name,
                    test_value,
                    reference_min,
                    reference_max,
                    unit
                FROM test_results
                WHERE report_id = %s
            """

            cursor.execute(
                test_query,
                (row["id"],)
            )

            test_rows = cursor.fetchall()

            tests = [
                TestResult(
                    name=test_row["test_name"],
                    value=float(test_row["test_value"]),
                    reference_min=(
                        float(test_row["reference_min"])
                        if test_row["reference_min"] is not None
                        else None
                    ),
                    reference_max=(
                        float(test_row["reference_max"])
                        if test_row["reference_max"] is not None
                        else None
                    ),
                    unit=test_row["unit"]
                )
                for test_row in test_rows
            ]

            reports.append(
                MedicalReport(
                    report_number=row["report_number"],
                    patient_id=row["patient_id"],
                    patient_name=row["patient_name"],
                    report_date=row["report_date"],
                    doctor=row["doctor"],
                    hospital=row["hospital"],
                    diagnosis=row["diagnosis"],
                    tests=tests
                )
            )

        return reports

    finally:
        cursor.close()
        connection.close()