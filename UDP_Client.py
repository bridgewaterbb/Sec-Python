#!/bin/python3

#Simple UDP Client

import socket


#Change these values
target_host = "127.0.0.1"
target_port = 9997

#create socket object
#AF_INET indicates we are using an IPv4 adress or host
#SOCK_DGRAM indicates connection is UPD
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#send data
#no connection request since UDP
client.sendto(b"AAABBBCCC",(target_host,target_port))

#receive data
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()
