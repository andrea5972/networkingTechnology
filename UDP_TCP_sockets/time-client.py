#!/usr/bin/env python3

import socket

import struct # Interpret bytes as packed binary data
import sys, time, datetime

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # The port used by the server

# socket.SOCK_STREAM == TCP Socket
# socket.SOCK_DGRAM == UDP Socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))  
    s.sendall(b'datetime')
    
    before_call  = datetime.datetime.now()
    print('before_call:', before_call)

    data = s.recv(1024)
    after_call = datetime.datetime.now()
    print('after_call:', after_call)
    milliseconds = after_call - before_call
  

print('milliseconds:', milliseconds)
print("to fetch:", repr(data))
s.close()
print(f"it took {milliseconds} to fetch {data}")
