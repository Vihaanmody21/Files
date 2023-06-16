import socket

Server = socket.socket()

Server.bind(("localhost", 9999))
Server.listen(3)
print("---Connections---")

while True:
    Client, Address = Server.accept()
    print(f"Connected With {Address}")
    Client.send(bytes("Server-Client Program Successful", "utf-8"))
    Client.close()