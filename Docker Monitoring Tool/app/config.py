LOG_FILES = ["/host/logs/syslog", "/host/logs/auth.log", "/host/logs/dmesg"]
KEYWORDS = ["unauthorized", "disk", "error", "shutdown"]
SCAN_INTERVAL = 60

EMAIL_SETTINGS = {
    "enabled": True,
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587,
    "sender": "you@example.com",
    "password": "yourpassword",
    "recipient": "alert@example.com"
}

TELEGRAM_SETTINGS = {
    "enabled": True,
    "bot_token": "YOUR_BOT_TOKEN",
    "chat_id": "YOUR_CHAT_ID"
}