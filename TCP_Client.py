#!/bin/python3

#Simple TCP Client
#Useful when you don't have network tools or internet access.

import socket

#Change Target
target_host = "0.0.0.0"
target_port = 9998

#Create a socket object
#AF_INET indicates we will use a standard IPv4 address or hostname.
#SOCK_STREAM indicates it will be a TCP client.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client or client server
client.connect((target_host,target_port))

#Send some data
#Change values after first \r\n.
client.send(b"GET / HTTP/1.1\r\nWe are watching you\r\n\r\n")

#Receive data
response = client.recv(4096)

print(response.decode())
client.close()
