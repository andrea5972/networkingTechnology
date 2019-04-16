#!/usr/bin/env python3

import http.server
import socketserver

PORT= 80
Handler = http.server.SimpleHTTPRequestHandler

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
        The request handler class for our server.
        """
    
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        #
        ip_port = self.request.getpeername()
        self.request.sendall((ip_port[0] + ":" + str(ip_port[1])).encode('utf-8'))


if __name__ == "__main__":
    HOST, PORT = "localhost", 80
    
    # Activate the http as server
    # To interrupt the program with Ctrl-C
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()
