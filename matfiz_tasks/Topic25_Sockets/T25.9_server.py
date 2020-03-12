import os
import socket

from os import path, mkdir, listdir, getcwd


CHUNKLIMIT = 2 ** 9


def copy_file(file_name, dir_in, dir_out):
    fulldir_in = path.join(dir_in, file_name)
    file_in = open(fulldir_in, 'rb')

    fulldir_out = path.join(dir_out, file_name)
    file_out = open(fulldir_out, 'wb')

    while True:
        data_in = file_in.read(CHUNKLIMIT)
        if not data_in:
            break
        file_out.write(data_in)

    file_in.close()
    file_out.close()


def copy_directory(dir_in, dir_out):
    folder_name = path.split(dir_in)[-1]
    elem_list = listdir(dir_in)

    fulldir_out = path.join(dir_out, folder_name)
    mkdir(fulldir_out)

    for elem in elem_list:
        elem_dir = path.join(dir_in, elem)
        if path.isfile(elem_dir):
            try: copy_file(elem, dir_in, fulldir_out)
            except Exception: print(f'skip {elem}.')
        else:
            copy_directory(dir_in, fulldir_out)


def get_backupname(bkp_dir):
    from datetime import datetime as dt
    current_time = dt.now()
    dir_suffix = current_time.strftime('%Y%m%d_%H%M%S')
    dir_name = 'backup_' + dir_suffix

    return path.join(bkp_dir, dir_name)


def backup_directories(dirs, bkp_dir):
    target_dir = get_backupname(bkp_dir)
    mkdir(target_dir)
    for d in dirs:
        try: copy_directory(d, target_dir)
        except Exception: print('skipped..')


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host, port = socket.gethostname(), 1919

sock.bind((host, port))
sock.listen()

connection, address = sock.accept()
print(">>> Connected to the", address, '\n...')

BACKUPDIR = connection.recv(1024).decode()
connection.send(b'received the BACKUP directory')

DIRECTORIES = []
while True:
    temp_dir = connection.recv(1024).decode()
    if not temp_dir:
        break
    DIRECTORIES.append(temp_dir)
    temp_name = path.split(temp_dir)[-1]
    connection.send(f"catalogue <{temp_name}> has been loaded successfully!".encode())

print('all directories have been added to the list')
print('now we have to create a backup in gotten directory from directories in the list...')
backup_directories(DIRECTORIES, BACKUPDIR)
print('Congratulations! Backup created!')
print("...\n>>> Disconnected from the", address)