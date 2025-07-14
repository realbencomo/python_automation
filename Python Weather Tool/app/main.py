import smtplib
from config import EMAIL_SETTINGS
from weather import fetch_weather

def send_email(subject, body):
    message = f"Subject: {subject}\n\n{body}"
    try:
        with smtplib.SMTP(EMAIL_SETTINGS["smtp_server"], EMAIL_SETTINGS["smtp_port"]) as server:
            server.starttls()
            server.login(EMAIL_SETTINGS["sender"], EMAIL_SETTINGS["password"])
            server.sendmail(EMAIL_SETTINGS["sender"], EMAIL_SETTINGS["recipient"], message)
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

def main():
    report = fetch_weather()
    send_email("This is your daily Weather Report", report)

if __name__ == "__main__":
    main()
# This script fetches the weather data and sends it via email.
