#!/bin/python3

#Simple, standard, multithreaded TCP Server
#Useful when writing command shells or crafting a proxy


import socket
import threading

#Change these values
IP = '0.0.0.0'
PORT = 9998


def main():
	
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#IP and Port server listens on
	server.bind((IP, PORT))
	#Tell server to listen w/ maximum backlog connections of X, 5 in this example.
	server.listen(5)
	print(f'[*] Listening on {IP}:{PORT}')
	
	while True:
	
		#Put server in main loop, wating for connections
		#When client accepts, client socket goes to client variable and remote connection goes to address variable	
		client, address = server.accept()
		print(f'[*] Accepted connection from {address[0]}:{address[1]}')
		#create new thread object which points at the handle_client function, pass this to the client socket as an argument
		client_handler = threading.Thread(target=handle_client, args=(client,))
		#Start thread to handle the connection
		#Main server loop ready to handle another connection
		client_handler.start()
	
#handle_client performs recv and sends message back to connecting client	
def handle_client(client_socket):
	with client_socket as sock:
		request = sock.recv(1024)
		print(f'[*] Received: {request.decode("utf-8")}')
		sock.send(b'ACK')
		

if __name__ == '__main__':
	main()
