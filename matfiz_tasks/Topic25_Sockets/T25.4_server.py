import socket
import re


def check_line(patt, someline):
    if re.fullmatch(patt, someline): res = f"Yes! << {someline} >> is e-mail."
    else: res = f"No! << {someline} >> is plaintext."

    return res


sock = socket.socket()
host = socket.gethostname()
port = 12345

sock.bind((host, port))
sock.listen(5)
conn, addr = sock.accept()

print('\n' + '*' * 60)
print("Connected to:", addr)
print('*' * 60 + '\n\n')

PATTERN = ''

while True:
    message = conn.recv(1024).decode()
    if not message: break

    if not PATTERN:
        PATTERN = message
        result = "Pattern has been received!\n"
    else:
        result = check_line(PATTERN, message)

    conn.send(result.encode())
