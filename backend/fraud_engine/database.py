import os

import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv


# Load variables from the .env file
load_dotenv()


DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", "3306")),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME", "meditrust")
}


def create_connection():
    """
    Create and return a connection to the MediTrust MySQL database.
    """

    try:
        connection = mysql.connector.connect(
            host=DB_CONFIG["host"],
            port=DB_CONFIG["port"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            database=DB_CONFIG["database"]
        )

        if connection.is_connected():
            print("MySQL connection successful.")
            return connection

    except Error as error:
        print("MySQL connection failed.")
        print("Error:", error)

    return None