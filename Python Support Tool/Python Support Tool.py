import os
import platform
import subprocess
import psutil

def show_menu():
    print("""
--- pySupportTool ---
1. Verify connectivity (ping)
2. System information
3. Clean temp files
0. Exit
""")

def ping_host():
    host = input("Input the domain or IP to ping: ")
    try:
        count = "-n" if platform.system().lower() == "windows" else "-c"
        subprocess.run(["ping", count, "4", host], check=True)
    except subprocess.CalledProcessError:
        print("Error: couldn't ping the provided host.")

def system_info():
    print("\n--- System information ---")
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"CPU: {platform.processor()}")
    print(f"Total RAM: {psutil.virtual_memory().total // (1024 ** 2)} MB")
    print(f"Available RAM: {psutil.virtual_memory().available // (1024 ** 2)} MB")
    print(f"Disk space: {psutil.disk_usage('/').free // (1024 ** 3)} GB disponibles\n")

def clean_temp_files():
    print("\n--- Basic cleaning ---")
    temp_dirs = ["/tmp", os.path.expanduser("~/.cache")] if platform.system() != "Windows" else [os.getenv('TEMP')]
    for path in temp_dirs:
        if os.path.exists(path):
            for root, dirs, files in os.walk(path):
                for name in files:
                    try:
                        os.remove(os.path.join(root, name))
                    except Exception:
                        pass
    print("Temp files cleaned.\n")

if __name__ == "__main__":
    while True:
        show_menu()
        option = input("Select an option: ")
        if option == "1":
            ping_host()
        elif option == "2":
            system_info()
        elif option == "3":
            clean_temp_files()
        elif option == "0":
            print("Closing...")
            break
        else:
            print("Invalid input. Try again.")