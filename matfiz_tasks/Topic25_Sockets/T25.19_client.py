import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host, port = socket.gethostname(), 2519

sock.connect((host, port))

