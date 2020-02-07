import socket
import os

backup_directory = os.getcwd()
os.chdir(os.path.dirname(os.getcwd()))
current_directory = os.getcwd()

# here you can add your own filenames
folder_list = [
    'Topic3_Loops',
    'Topic5_Strings',
    'Topic6_Lists',
    'Topic8_Dictionaries',
    'Topic9_Functions'
]
folder_list = [os.path.join(current_directory, elem) for elem in folder_list]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host, port = socket.gethostname(), 1919

sock.connect((host, port))
sock.send(backup_directory.encode())
answer = sock.recv(1024).decode()
print(answer)

for i, d in enumerate(folder_list):
    sock.send(d.encode())
    ans = sock.recv(1024).decode()
    print(ans)

sock.close()

