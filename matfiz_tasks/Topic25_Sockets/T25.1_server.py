import socket
import re
import os


s = socket.socket()
host = socket.gethostname()
port = 12345

s.bind((host, port))

s.listen(5)

# dir_path = os.path.dirname(os.path.realpath(__file__))
# print(dir_path)
# fin = open(dir_path + '\\' + "T25.1_file.txt", r)
fin = open("T25.1_file.txt", 'r')

datalist = fin.readlines()

D1 = r'\d{1,2}\.\d{1,2}\.\d{4}'
D2 = r'\d{4}-\d{1,2}-\d{1,2}'
D3 = r'\d{1,2}/\d{1,2}/\d{4}'
P_DATE = D1+'|'+D2+'|'+D3
cp_d = re.compile(P_DATE)

output = ''
for d in datalist:
    if re.findall(P_DATE, d):
        d = d.replace('-', '.').replace('/', '.')
        output += str(d)

while True:
    c, addr = s.accept()
    print ('got connecton from address:', addr)

    out = str(output)
    c.send(out.encode())
    c.close()
