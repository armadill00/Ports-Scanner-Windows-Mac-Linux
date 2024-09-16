This Python script scans for open ports on a system and identifies the services running on those ports. It uses psutil to retrieve process information and can map custom services to specific ports. The program is compatible with Linux, macOS, and Windows.

<b>Features:</b>
Platform Support: Works on Linux, macOS, and Windows.
Custom Port Mapping: Allows you to define custom service mappings for specific ports (e.g., SharePoint for port 42050).
Process Lookup: Automatically retrieves the name of the process running on a port using psutil.
Netstat-based Scanning: Utilizes platform-specific netstat commands to find open ports.
Error Handling: Provides feedback if there are issues running system commands.
Usage:
Clone the repository and run the script.
The program scans for open ports and displays a list of ports along with the services/processes bound to them.
Example Output:
markdown
Copy code
Port      Service
------------------------------
80        Apache
443       nginx
42050     Microsoft.SharePoint.exe
Requirements:
Python 3.x
psutil library
Installation:
Install the required psutil library:
bash
Copy code
pip install psutil
Run the script:
bash
Copy code
python port_scanner.py
Custom Port Mapping:
You can add or modify the custom port-to-service mappings by editing the CUSTOM_SERVICE_MAPPING dictionary in the script.
