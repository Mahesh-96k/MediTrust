from database import create_connection


connection = create_connection()


if connection:
    print("PASS: MediTrust database connection is working.")

    connection.close()
    print("MySQL connection closed.")
else:
    print("FAIL: Could not connect to MediTrust database.")