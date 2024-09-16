This Python script scans for open ports on a system and identifies the services running on those ports. It uses psutil to retrieve process information and can map custom services to specific ports. The program is compatible with Linux, macOS, and Windows.

##Features:
* Platform Support: Works on Linux, macOS, and Windows.
* Custom Port Mapping: Allows you to define custom service mappings for specific ports (e.g., SharePoint for port 42050).
* Process Lookup: Automatically retrieves the name of the process running on a port using psutil.
* Netstat-based Scanning: Utilizes platform-specific netstat commands to find open ports.
* Error Handling: Provides feedback if there are issues running system commands.
##Usage:
* Clone the repository and run the script.
* The program scans for open ports and displays a list of ports along with the services/processes bound to them.
