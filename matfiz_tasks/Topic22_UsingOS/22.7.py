import os
import datetime


def searcholdfile(dir):
    d = {}

    for root, listdir, listfiles in os.walk(dir):
        for i in listfiles:
            t = os.path.getctime(os.path.join(root, i))
            time = datetime.datetime.fromtimestamp(t)
            d[i] = time

    for i in d:
        if d[i] == min(d.values()):
            print(i, min(d.values()))


if __name__ == '__main__':
    dirname_1 = r'D:\programming\Matfiz'
    dirname_2 = r'C:\Users\The Godfather\Documents'
    searcholdfile(dirname_1)
    searcholdfile(dirname_2)
