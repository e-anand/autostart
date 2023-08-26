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

