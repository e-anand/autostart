import subprocess
import datetime
import time


def is_process_running(process_name):
    try:
        result = subprocess.run(['tasklist', '/FI', f'IMAGENAME eq {process_name}'], capture_output=True, text=True)
        return process_name.lower() in result.stdout.lower()
    except:
        return False

def restart_process(process_path):
    try:
        subprocess.Popen(process_path)
    except:
        pass

def log_event(event):
    with open("chrome_log.txt", "a") as log_file:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{timestamp}] {event}\n")
start_time = datetime.time(9, 0)     # Specify the start time (9:00 AM)
end_time = datetime.time(15, 30)     # Specify the end time (3:30 PM)


if __name__ == "__main__":
    process_name = "firefox.exe"
    process_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe" 
    
    while True:
        current_time = datetime.datetime.now().time()        
        if start_time <= current_time <= end_time:
            if not is_process_running(process_name):
                print("firefox is not running. Restarting...")
                log_event("firefox went down.")
                restart_process(process_path)
            time.sleep(.1)

def start_process(process_path):
    try:
        subprocess.Popen(process_path)
        print(f"Started {process_path}")
    except Exception as e:
        print(f"Error starting {process_path}: {e}")

process_name = "Moneymaker.exe"  # Update with the actual process name
process_path = r"C:\path\to\Moneymaker.exe"  # Update with the actual path to the executable


while True:
    current_time = datetime.datetime.now().time()
    
    if start_time <= current_time <= end_time:
        if not is_process_running(process_name):
            start_process(process_path)
    else:
        print("Outside of monitoring time window.")
        break  # Exit the loop if outside the time window
    
    time.sleep(1)  # Wait for 1 second before checking again
