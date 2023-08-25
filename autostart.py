import psutil
import subprocess
import datetime
import time

def is_process_running(process_name):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            return True
    return False

def start_process(process_path):
    try:
        subprocess.Popen(process_path)
        print(f"Started {process_path}")
    except Exception as e:
        print(f"Error starting {process_path}: {e}")

process_name = "Moneymaker.exe"  # Update with the actual process name
process_path = r"C:\path\to\Moneymaker.exe"  # Update with the actual path to the executable

start_time = datetime.time(9, 0)     # Specify the start time (9:00 AM)
end_time = datetime.time(15, 30)     # Specify the end time (3:30 PM)

while True:
    current_time = datetime.datetime.now().time()
    
    if start_time <= current_time <= end_time:
        if not is_process_running(process_name):
            start_process(process_path)
    else:
        print("Outside of monitoring time window.")
        break  # Exit the loop if outside the time window
    
    time.sleep(1)  # Wait for 1 second before checking again