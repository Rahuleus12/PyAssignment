import psutil
import time

def monitor_cpu(threshold=80, check_interval=1):
    """
    Monitors CPU usage and alerts if it exceeds the predefined threshold.

    :param threshold: The CPU usage percentage to trigger an alert.
    :param check_interval: The time interval (in seconds) between checks.
    """
    print("Monitoring CPU usage... Press Ctrl+C to stop.")
    try:
        while True:
            # Get the current CPU usage as a percentage
            cpu_usage = psutil.cpu_percent(interval=0.1)

            # Check if the CPU usage exceeds the threshold
            if cpu_usage > threshold:
                print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")

            # Wait for the next check
            time.sleep(check_interval)
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    # Define the CPU usage threshold and monitoring interval (in seconds)
    threshold = 80  # You can change this value as needed
    check_interval = 1  # Adjust the interval based on requirements

    monitor_cpu(threshold, check_interval)

# python cpu_monitor.py
