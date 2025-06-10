import socket
from datetime import datetime
from time_test import Timer

timing = Timer()

print("enter your target IP address:")
target=socket.gethostbyname(input("IP address: "))

open_ports = []
for i in range(1, 100):
    try:
        # Create a socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a timeout of 1 second
        # Attempt to connect to the target IP on port i
      
        timing.sleep(0.1)  # Sleep for 0.1 seconds between scans
        result = sock.connect_ex((target, i))
        if result == 0:
            open_ports.append(i)
            print(f"Port {open_ports} is open",sep=" ")
        
            
    except socket.error as e:
        print(f"Error connecting to port {i}: {e}")
    finally:
        sock.close()
    
print(f"Time taken to scan ports: {timing.elapsed():.2f} seconds")
with open("port_scan_results.txt", "a+") as file:
    file.write(f"Port scan results for {target} on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write(f"Time taken to scan ports: {timing.elapsed():.2f} seconds\n")
    file.write(f"ports found open: {open_ports}\n")
    file.write("-"*50+"\n")
    
