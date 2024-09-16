import socket
import subprocess
import platform
import psutil

# Custom port-to-service mapping
CUSTOM_SERVICE_MAPPING = {
    42050: "Microsoft.SharePoint.exe"
}

def get_service_name(port):
    """Returns the name of the service running on a given port, with custom overrides."""
    if port in CUSTOM_SERVICE_MAPPING:
        return CUSTOM_SERVICE_MAPPING[port]
    
    for conn in psutil.net_connections():
        if conn.laddr.port == port:
            try:
                return psutil.Process(conn.pid).name()
            except psutil.NoSuchProcess:
                return "Unknown (Process not found)"
    return "Unknown Service"

def get_open_ports():
    system = platform.system()

    if system == 'Linux' or system == 'Darwin':
        command = "netstat -tuln | grep LISTEN"
    elif system == 'Windows':
        command = "netstat -an | findstr LISTENING"
    else:
        raise OSError("Unsupported OS: " + system)

    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if result.returncode != 0:
        print("Error while running command:", result.stderr.decode())
        return []
    
    open_ports = []
    output = result.stdout.decode()

    for line in output.splitlines():
        parts = line.split()
        if system == 'Linux' or system == 'Darwin':
            address = parts[3]  # Extract the address column
        elif system == 'Windows':
            address = parts[1]  # Extract the address column
        
        port = int(address.split(":")[-1])  # Extract the port number and convert to integer
        open_ports.append(port)

    return open_ports

if __name__ == "__main__":
    print("Scanning for open internet ports...")
    open_ports = get_open_ports()
    
    if open_ports:
        print(f"{'Port':<10}{'Service'}")
        print("-" * 30)
        for port in open_ports:
            service = get_service_name(port)
            print(f"{port:<10}{service}")
    else:
        print("No open ports found.")
