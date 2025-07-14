import os
from dotenv import load_dotenv

load_dotenv()

CITY = os.getenv("CITY")
API_KEY = os.getenv("API_KEY")
EMAIL_SETTINGS = {
    "sender": os.getenv("EMAIL_SENDER"),
    "password": os.getenv("EMAIL_PASSWORD"),
    "recipient": os.getenv("EMAIL_RECIPIENT"),
    "smtp_server": os.getenv("SMTP_SERVER"),
    "smtp_port": os.getenv("SMTP_PORT", 587)  # Default to
}

# This script is responsible for loading config values from the .env file :D