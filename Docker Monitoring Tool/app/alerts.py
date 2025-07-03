import smtplib
import requests
from config import EMAIL_SETTINGS, TELEGRAM_SETTINGS

def send_email_alert(subject, body):
    if not EMAIL_SETTINGS["enabled"]:
        return
    message = f"Subject: {subject}\n\n{body}"
    try:
        with smtplib.SMTP(EMAIL_SETTINGS["smtp_server"], EMAIL_SETTINGS["smtp_port"]) as server:
            server.starttls()
            server.login(EMAIL_SETTINGS["sender"], EMAIL_SETTINGS["password"])
            server.sendmail(EMAIL_SETTINGS["sender"], EMAIL_SETTINGS["recipient"], message)
    except Exception as e:
        print(f"[ERROR] Failed to send email: {e}")

def send_telegram_alert(message):
    if not TELEGRAM_SETTINGS["enabled"]:
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_SETTINGS['bot_token']}/sendMessage"
    payload = {"chat_id": TELEGRAM_SETTINGS["chat_id"], "text": message}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"[ERROR] Failed to send Telegram message: {e}")