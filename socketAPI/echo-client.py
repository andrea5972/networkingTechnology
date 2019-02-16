#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')

    data = s.recv(1024) #the bufsize arg of 1024 is the max amount
                        #of data to be received at once 

print('Received', repr(data))