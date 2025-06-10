import socket
from datetime import datetime
from time_test import Timer
import threading

timing = Timer()

print("Enter your target IP address:")
target = socket.gethostbyname(input("IP address: "))

open_ports = []
lock = threading.Lock()
max_threads = 300
threads = []

def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)  # fast timeout
    try:
        result = sock.connect_ex((target, port))
        if result == 0:
            with lock:
                open_ports.append(port)
                print(f"Port {port} is open")
    except socket.error:
        pass
    finally:
        sock.close()

# Scan ports 1 to 1024 (or go higher if you want)
for port in range(1, 1025):
    # Throttle: only allow up to `max_threads` running at a time
    while threading.active_count() > max_threads:
        pass

    t = threading.Thread(target=scan_port, args=(port,))
    t.start()
    threads.append(t)

# Wait for all threads to finish
for t in threads:
    t.join()

# Save results
print(f"\nScan complete in {timing.elapsed():.2f} seconds")
with open("port_scan_results2.txt", "a+") as file:
    file.write(f"Port scan results for {target} on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write(f"Time taken to scan ports: {timing.elapsed():.2f} seconds\n")
    file.write(f"Ports found open: {sorted(open_ports)}\n")
    file.write("-" * 50 + "\n")
