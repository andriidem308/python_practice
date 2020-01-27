import os
import datetime


def searcholdfile(dir):
    d = {}  # Создаем словарь, куда будем засовывать файлы и их даты изменения

    # os.walk(directory) - возвращает последовательность кортежей всех подкаталогов
    # По простому: "отдает" список из всех подпапок в указанной директории (directory)
    # Каждую подпапку описывает кортеж (КАТАЛОГ, СПИСОК ПОДКАТАЛОГОВ, СПИСОК ФАЙЛОВ КАТАЛОГА)
    # Обозначениями: (dirpath, dirnames, filenames).
    # В цикле ниже root выступает в качестве dirpath (КАТАЛОГА),
    # listdir - dirnames (СПИСКА ПОДКАТАЛОГОВ) , listfiles - filenames (СПИСКА ФАЙЛОВ В dirnames).
    for root, listdir, listfiles in os.walk(dir):
        # ниже цикл проходит по каждому файлу из СПИСКА ФАЙЛОВ (listfiles)
        for i in listfiles:
            # Тут сложно не запутаться:
            # Вот эта вся команда возвращает дату создания файла 'i'
            t = os.path.getctime(os.path.join(root, i))
            # Тут оно преобразовывается в время
            time = datetime.datetime.fromtimestamp(t)
            # И это время мы кидаем в словарь
            d[i] = time

    # Здесь мы находим файл с мин. временем, что значит самый старый файл
    for i in d:
        if d[i] == min(d.values()):
            print(i, min(d.values()))


if __name__ == '__main__':
    dirname = r'C:\Users\morgu\.PyCharm2019.2\config\scratches\22.1.1'
    searcholdfile(dirname)
