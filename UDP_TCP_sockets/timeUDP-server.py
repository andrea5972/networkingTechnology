#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        #Port to listen on (non-privileged ports are > 1023)

# socket.SOCK_STREAM == TCP Socket
# socket.SOCK_DGRAM == UDP Socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()      #makes a listening socket 
    conn, addr = s.accept()  
    with conn:
        print('Client connection', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

