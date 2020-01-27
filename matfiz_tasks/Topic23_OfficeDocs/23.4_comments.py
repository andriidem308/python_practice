from docx import Document
import re
import datetime

# нижние подчеркивание - (НП); точка - (Т)
# Шаблон __.__.____ - 2НП-Т-2НП-Т-4НП
# число в { } - кол-во повторений символа перед скобками
# \. - точка
pattern = r"\_{2}\.\_{2}\.\_{4}"
# \d - цифра --> Шаблон: 11.11.1111, надеюсь понял.
pattern2 = r"\d{2}\.\d{2}\.\d{4}"

# Название файла, который потом открываем,
# вводим с клавы и запихиваем в переменную filename
filename = input("Enter the filename(.docx): ")

# открываем файл с названием filename
document = Document(filename)

# создаем пустой список, сюда будем запихивать даты
dates = []

# Перебираем каждую СТРОКУ (или ПАРАГРАФ, так и так можно) в документе
for paragraph in document.paragraphs:
    # Для каждой строки выполняем
    for run in paragraph.runs:
        text = run.text  # сводим текст к норм виду и записываем в text
        # print(text)
        # Условие, если в строке есть хотя бы один наш заданный шаблон (11.11.1111)
        if (re.findall(pattern2, text) != []):
            dates.append(re.findall(pattern2, text))  # Тогда добавляем его в список всех дат
        currDate = datetime.datetime.today().strftime("%d.%m.%Y")  # получаем текущую дату в формате 11.11.1111 (ДД.ММ.ГГГГ)
        result = re.sub(pattern, currDate, text)  # меняем в text все __.__.____ на текущую дату
        run.text = result  # меняем это в строке документа ( перед этим было в переменной )


print("Dates: ")
# dates - это по сути список из списков, то есть не просто [], а [[], [], [], ..., []]
# в каждом внутреннем списке содержаться даты и вот в двойном цикле ниже
# мы все эти даты выводим
for i in dates:
    for j in i:
        print(j)

# Сохраняем измененный документ
document.save(filename)
