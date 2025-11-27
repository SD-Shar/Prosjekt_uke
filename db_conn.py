import os
import mysql.connector
from dotenv import load_dotenv

# Last inn .env-filen slik at miljøvariabler blir tilgjengelige
load_dotenv()

def get_connection():
    """Returnerer en aktiv database-tilkobling basert på miljøvariabler."""
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST", "localhost"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        database=os.environ.get("DB_NAME")
    )
