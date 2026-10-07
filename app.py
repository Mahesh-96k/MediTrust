from flask import Flask, render_template, request
import mysql.connector
from werkzeug.utils import secure_filename
import os
import uuid 
app = Flask(__name__)
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Akash@123",
    database="meditrust"
)
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf", "jpg", "jpeg", "png"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )
    
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login")
def login():
    return render_template("login.html")
@app.route("/verification/<report_id>")
def verification(report_id):

    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            reports.*,
            verification_results.patient_name,
            verification_results.doctor_name,
            verification_results.hospital_name,
            verification_results.diagnosis,
            verification_results.report_date,
            verification_results.laboratory_results,
            verification_results.validation_findings,
            verification_results.risk_score,
            verification_results.risk_level,
            verification_results.risk_reasons
        FROM reports
        LEFT JOIN verification_results
        ON reports.report_id = verification_results.report_id
        WHERE reports.report_id = %s
    """, (report_id,))

    report = cursor.fetchone()

    cursor.close()

    if not report:
        return "Report not found."

    return render_template(
        "verification.html",
        report=report
    )
@app.route("/dashboard")
def dashboard():

    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM reports ORDER BY upload_time DESC")

    reports = cursor.fetchall()

    cursor.close()

    total_reports = len(reports)

    return render_template(
        "dashboard.html",
        reports=reports,
        total_reports=total_reports
    )
    
@app.route("/upload", methods=["GET", "POST"])
def upload():

    if request.method == "POST":

        file = request.files.get("report")

        if not file or file.filename == "":
            return "No file selected."

        if not allowed_file(file.filename):
            return "Invalid file type. Please upload PDF, JPG, JPEG or PNG."

        original_filename = secure_filename(file.filename)

        unique_part = uuid.uuid4().hex[:8].upper()

        report_id = "MT-" + unique_part

        saved_filename = report_id + "_" + original_filename

        file_path = os.path.join(
            app.config["UPLOAD_FOLDER"],
            saved_filename
        )

        file.save(file_path)

        cursor = db.cursor()

        sql = """
        INSERT INTO reports
        (report_id, original_filename, saved_filename, status)
        VALUES (%s, %s, %s, %s)
        """

        values = (
            report_id,
            original_filename,
            saved_filename,
            "Uploaded"
        )

        cursor.execute(sql, values)
        db.commit()

        cursor.close()

        print("Report ID:", report_id)
        print("File saved:", file_path)

        return f"Upload successful! Report ID: {report_id}"

    return render_template("upload.html")

if __name__ == "__main__":
    app.run(debug=True)