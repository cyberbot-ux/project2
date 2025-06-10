import socket
from datetime import datetime
from time_test import Timer
import threading
import os
import time
timing = Timer()

print("Enter your target IP address:")
target = socket.gethostbyname(input("IP address: "))

open_ports = []
lock = threading.Lock()
max_threads = os.cpu_count() * 50  # Use a multiple of CPU cores for better performance
threads = []

def scan_port(port):
    common_ports = {
    20: 'FTP-Data', 21: 'FTP', 22: 'SSH', 23: 'Telnet', 25: 'SMTP',
    53: 'DNS', 80: 'HTTP', 110: 'POP3', 143: 'IMAP', 443: 'HTTPS',
    3306: 'MySQL', 3389: 'RDP'
                    }



    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)  # fast timeout
    try:
        result = sock.connect_ex((target, port))
        if result == 0:
            with lock:
                service = common_ports.get(port, 'Unknown')
                open_ports.append(port)
                print(f"Port {port} ({service}) is open")
    
    except socket.error:
        pass
    finally:
        sock.close()

# Scan ports 1 to 1024 (or go higher if you want)
for port in range(1, 1025):
    # Throttle: only allow up to `max_threads` running at a time
    while threading.active_count() > max_threads:
        time.sleep(0.01)  # Sleep briefly to avoid busy waiting    
    

    t = threading.Thread(target=scan_port, args=(port,))
    t.start()
    threads.append(t)

# Wait for all threads to finish
for t in threads:
    t.join()

# Save results
print(f"\nScan complete in {timing.elapsed():.2f} seconds")
with open("port_scan_results_3.txt", "a+") as file:
    file.write(f"Port scan results for {target} on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write(f"Time taken to scan ports: {timing.elapsed():.2f} seconds\n")
    file.write(f"Ports found open: {sorted(open_ports)}\n")
    file.write("-" * 50 + "\n")
