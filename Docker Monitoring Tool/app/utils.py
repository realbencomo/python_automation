import re
import os

def check_logs(log_files, keywords):
    matched = []
    for file_path in log_files:
        if not os.path.exists(file_path):
            continue
        with open(file_path, "r", errors="ignore") as file:
            lines = file.readlines()
            for line in lines[-500:]:
                for keyword in keywords:
                    if re.search(keyword, line, re.IGNORECASE):
                        matched.append((file_path, line.strip()))
    return matched