import socket

target = input("Enter IP Address: ")
ports = [21,22,23,53,80,443,1433,3000,8080]

print(f"Scanning {target} \n")

for port in ports:
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
