import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 1234  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024)
    print(str(data.decode()))
    select=input("enter your choice :\n")
    s.send(select.encode())
    time = s.recv(1024)
    print(str(time.decode()))