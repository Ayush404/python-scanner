#!/bin/python

import sys
import socket
from datetime import datetime

#Define our target

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])  #Translates hostname to ipv4

else:
    print('''Invalid Syntax
Syntax : python scanner.py <ip>''' )

#Adding a banner
print("-"*50)
print(f'Scanning target : {target}')
print(f'Time started : {datetime.now()}')
print("-"*50)

try:
    for port in range(1,1000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))  #return an error indicator
        print(f'Checking port : {port}')
        if result == 0:
            print(f'Port {port} is open')
        s.close()

except KeyboardInterrupt:
    print("\n Exiting program")
    sys.exit()
except socket.gaierror:
    print("Hostname resolution failed. Try giving a correct one")
    sys.exit()
except socket.error:
    print("Connection to server failed")
    sys.exit()

