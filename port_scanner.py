import socket
from datetime import datetime

#TCP 
def scan_tcp_port(target,port,file):
    try: 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target,port))

        try:
            service= socket.getservbyport(port)
        except:
            service= "Unknown"

        if result == 0:
            status = f"Port {port} ({service}) is Open\n"
        elif result == 111 or result == 10061:
            status = f"Port {port} ({service}) is Closed\n"
        else:
            status = f"Port {port} ({service}) is Filtered or Unreachable (code: {result})\n"

        print(status)
        file.write(status)
        s.close()
    except Exception as e:
        error = f"Error in scanning port {port} : {e}"
        print(error)
        file.write(error)

#UDP 
def scan_udp_port(target,port,file):
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.settimeout(2)
        s.sendto(b"",(target,port))
        
        try:
            data, _=s.recvfrom(1024)
            status = f"UDP port {port} seems Open or Responding\n"
        except socket.timeout:
            status= f"UDP port {port} is Open|Filtered (no response)\n"
        
        print (status)
        file.write(status)
        s.close()
    except Exception as e:
        error = f"Error scanning UDP port {port}: {e}\n"
        print (error)
        file.write(error)

#Main 
target = input("Enter Host name or  IP Address: ")

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid Host ...!") 
    exit()
    
print("Choose scan mode :")
print("1. Default ports :21,22,23,53,80,443")
print("2. Custom range of ports :")
print("3. Custom single port :")

choice = input("Enter yout choice (1/2/3):")
if choice == '1':
    ports = [21,22,23,53,80,443]
elif choice == '2':
    start_port = int(input("Enter start port :"))
    end_port = int(input("Enter end port :"))
    ports = range (start_port,end_port+1)
elif choice == '3':
    port = int(input("Enter port ton scan :"))
    ports = [port]
else:
    print("Invalid choice... !")
    exit()
print(f"Scanning {target} \n")

print("Enter scan type :")
print("1. TCP only")
print("2. UDP only")
print("3. Both TCP and UDP")
scan_type = input("Enter choice (1/2/3): ")

filename = f"Scan_{target}_{datetime.now().strftime("%Y-%m-%d %H-%M-%S")}.txt"

with open(filename,"w") as f:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    f.write(f"Scan started at : {timestamp} \n\n")
    f.write(f"Scan result for {target}:\n\n")
    for port in ports:
        if scan_type == '1':
            scan_tcp_port(target_ip, port, f)
        elif scan_type == '2':
            scan_udp_port(target_ip, port, f)
        elif scan_type == '3':
            scan_tcp_port(target_ip, port, f)
            scan_udp_port(target_ip, port, f)
        else :
            print("Invalid scan type ...!")
            break

print(f"\nScan completed and result saved in file {filename}")



            
        
