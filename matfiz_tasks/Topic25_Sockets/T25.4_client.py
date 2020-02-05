import socket
import re


pattern = r'(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)'
file = open("T25.4_file.txt")

sock = socket.socket()
host, port = socket.gethostname(), 12345

sock.connect((host, port))
sock.send(pattern.encode())

msg = sock.recv(1024).decode()
print(msg)

for line in file:
    sock.send(line.split()[0].encode())
    msg = sock.recv(1024).decode()
    print(msg)

sock.close()



