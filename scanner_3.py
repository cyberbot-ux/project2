import socket
from datetime import datetime
from time_test import Timer
import threading
import os
import time

# Start timer to measure total scan time
timing = Timer()

# Ask user for IP address to scan
print("Enter your target IP address:")
target = socket.gethostbyname(input("IP address: "))

# Shared list for storing open ports
open_ports = []

# Lock for thread-safe updates to open_ports
lock = threading.Lock()

# Determine max number of threads based on CPU cores (for performance)
max_threads = os.cpu_count() * 50
threads = []

# Function to scan a single port
def scan_port(port):
    # Dictionary of common ports and their service names
    common_ports = {
        20: 'FTP-Data', 21: 'FTP', 22: 'SSH', 23: 'Telnet', 25: 'SMTP',
        53: 'DNS', 80: 'HTTP', 110: 'POP3', 143: 'IMAP', 443: 'HTTPS',
        3306: 'MySQL', 3389: 'RDP'
    }

    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)  # Quick timeout for responsiveness
    try:
        # Attempt to connect to the port
        result = sock.connect_ex((target, port))
        if result == 0:
            # If connection successful, mark port as open
            with lock:
                service = common_ports.get(port, 'Unknown')
                open_ports.append(port)
                print(f"Port {port} ({service}) is open")
    except socket.error:
        pass  # Ignore socket errors silently
    finally:
        sock.close()

# Start scanning ports 1 to 1024
for port in range(1, 1025):
    # If too many threads are active, wait briefly
    while threading.active_count() > max_threads:
        time.sleep(0.01)

    # Create and start a new thread for this port
    t = threading.Thread(target=scan_port, args=(port,))
    t.start()
    threads.append(t)

# Wait for all threads to finish
for t in threads:
    t.join()

# Print and save scan results
print(f"\nScan complete in {timing.elapsed():.2f} seconds")
with open("port_scan_results_3.txt", "a+") as file:
    file.write(f"Port scan results for {target} on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write(f"Time taken to scan ports: {timing.elapsed():.2f} seconds\n")
    file.write(f"Ports found open: {sorted(open_ports)}\n")
    file.write("-" * 50 + "\n")
