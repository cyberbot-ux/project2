# Port Scanner Suite (Final Version: `scanner_3.py`)

This repository contains multiple versions of a Python-based port scanner developed for learning and experimentation. The final and most advanced version is **`scanner_3.py`**, which incorporates multi-threading, system-optimized performance, and common service name resolution.

---

## 🧠 Project Overview

A port scanner is used to identify open TCP ports on a target machine. This tool allows you to:

- Scan a range of ports (default: 1–1024)
- Use threading for faster scans
- Identify commonly known services on open ports
- Save scan results to a log file with timestamps

---

## 📁 Files Included

| File Name         | Description |
|------------------|-------------|
| `scanner_3.py`   | ✅ Final version – optimized with threading, port-to-service mapping, and efficient CPU usage |
| `scanner2.py`    | Intermediate version with basic multithreading |
| `scann.py`       | First version – single-threaded scan with delay |
| `time_test.py`   | Utility module to track time and handle delays |

---

## ✅ How to Use

### 1. Requirements

- Python 3.x
- Works on Windows, Linux, and macOS
- No external libraries required

### 2. Run the Scanner

```bash
python scanner_3.py
```

Enter the target IP address when prompted (e.g., `scanme.nmap.org` or `192.168.1.1`).

### 3. Output

- Open ports and their associated service names are displayed in the terminal.
- Results are saved in `port_scan_results_3.txt`.

---

## 🔁 Version Comparison

| Feature                     | `scann.py`   | `scanner2.py` | `scanner_3.py` |
|----------------------------|--------------|----------------|----------------|
| Port Range                 | 1–99         | 1–1024         | 1–1024         |
| Threading                  | ❌ No         | ✅ Yes (300)    | ✅ Yes (CPU-based) |
| Service Name Mapping       | ❌ No         | ❌ No           | ✅ Yes         |
| Delay per Scan             | ✅ 0.1s       | ❌ No           | ❌ No          |
| Performance                | 🐢 Slow       | 🚀 Fast         | ⚡ Super Fast  |
| Output File                | `port_scan_results.txt` | `port_scan_results2.txt` | `port_scan_results_3.txt` |

---

## 🔍 How They Work – Technical Differences

### 🔹 `scann.py` – Basic Single-threaded Scanner

- **Approach**: Loops through ports one by one (1–99).
- **Delay**: Sleeps for 0.1 seconds between scans to avoid overwhelming the system.
- **Speed**: Very slow.
- **Output**: Writes basic results (open ports + time taken) to a text file.
- **Best For**: Beginners learning how socket connections work.

---

### 🔹 `scanner2.py` – Multithreaded Scanner

- **Approach**: Uses Python `threading` to scan up to 1024 ports simultaneously.
- **Thread Cap**: Fixed thread limit of 300.
- **Speed**: Significantly faster than `scann.py`.
- **Thread Safety**: Uses locks to safely update the shared `open_ports` list.
- **Output**: More detailed, still lacks service identification.
- **Best For**: Learning how threading boosts scan speed.

---

### 🔹 `scanner_3.py` – Final Optimized Version

- **Approach**: Uses threads with a dynamic limit based on the number of CPU cores (`os.cpu_count() * 50`).
- **Service Mapping**: Includes common port-to-service mapping (e.g., 80 → HTTP).
- **Performance**: Most efficient and stable.
- **Output**: Clean logs with port numbers and service names.
- **Best For**: Practical use cases, clean code structure, optimized performance.

---

## 🔒 Disclaimer

This tool is intended **for educational purposes only**. Use it only on networks and devices you own or have explicit permission to test.

---

## 📌 Author

Made with 💻 by a cybersecurity student learning by building real-world tools.
