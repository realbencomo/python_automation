import time
from config import LOG_FILES, KEYWORDS, SCAN_INTERVAL
from utils import check_logs
from alerts import send_email_alert, send_telegram_alert

def main():
    print("[INFO] Starting Log Monitor...")
    while True:
        matches = check_logs(LOG_FILES, KEYWORDS)
        if matches:
            alert_msg = "\n".join([f"[{fp}] {line}" for fp, line in matches])
            send_email_alert("Log Monitor Alert", alert_msg)
            send_telegram_alert(alert_msg)
            print("[ALERT] Notification sent.")
        else:
            print("[INFO] No alerts found.")
        time.sleep(SCAN_INTERVAL)

if __name__ == "__main__":
    main()