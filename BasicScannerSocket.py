import socket

def scan_port(target,port):
    try: 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print(f"Port {port} is Open")
        elif result == 111 or result == 10061:
            print(f"Port {port} is Closed")
        else:
            print(f"Port {port} is Filtered or Unreachable (code: {result})")
        s.close()
    except Exception as e:
        print("Error in scanning port {port} : {e}")


target = input("Enter Host name or  IP Address: ")
try:
    target = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid Host ...!") 
    
print("Choose scan mode :")
print("1. Default ports :21,22,23,53,80,443,1433,3000,8080")
print("2. Custom range of ports :")
print("3. Custom single port :")

choice = input("Enter yout choice (1/2/3):")
if choice == '1':
    ports = [21,22,23,53,80,443,1433,3000,8080]
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

for port in ports:
    scan_port(target,port)
        
