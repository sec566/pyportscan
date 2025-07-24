# 🔍 Port Scanner in Python

A simple yet flexible **TCP Port Scanner** built with Python using the `socket` module.  
This tool allows users to scan default ports, a custom range, or a single port for any target host or IP address.

---

## 📦 Features

- Scan common default ports (21, 22, 23, 53, 80, 443, etc.)
- Scan a **custom port range** or a **single custom port**
- Displays whether each port is:
  - Open
  - Closed
  - Filtered or unreachable
- Saves scan results to a timestamped `.txt` file
- Handles hostname-to-IP resolution and input errors gracefully

---

## 🛠 Requirements

- Python 3.x  
(Recommended: Python ≥ 3.6 for `f-strings` and `datetime` support)

---

## 🚀 How to Use

1. **Clone the Repository** or download the script:
   ```bash
   git clone https://github.com/your-username/port-scanner.git
   cd port-scanner
Run the Script:

python BasicScannerSocket.py
Follow the Prompts:

Enter a valid IP address or domain name.

Choose one of the scanning modes:

Default ports

Custom port range

Single port

View Results:

Output is shown in the terminal.

Results are saved in a file like:
Scan_google.com_2025-07-24 17:53:12.txt

📝 Example
Enter Host name or IP Address: google.com
Choose scan mode :
1. Default ports :21,22,23,53,80,443,1433,3000,8080
2. Custom range of ports :
3. Custom single port :
Enter your choice (1/2/3): 1

Scanning google.com...

Port 80 is Open
Port 443 is Open
Port 21 is Closed
...
📁 Output File Example

Scan started at : 2025-07-24 17:53:12

Scan result for google.com:

Port 80 is Open
Port 443 is Open
Port 21 is Closed
...
🤖 How It Works
Uses Python’s socket module to create TCP connections

Each port is scanned using socket.connect_ex() to detect its status

Results are printed and saved simultaneously

Invalid hostnames are handled with socket.gaierror

Ports are scanned one at a time with a 1-second timeout

📌 Notes
This tool is meant for educational and ethical use only.
Never scan targets without permission.

To improve speed, you could implement multi-threading in the future.

🛡️ License
This project is open-source and available under the MIT License.

👨‍💻 Author
Created by [Your Name or GitHub Username]

Contributions, feedback, or suggestions are welcome!
