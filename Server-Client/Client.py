import socket

Client = socket.socket()

Client.connect(("localhost", 9999))
print(Client.recv(1024).decode())