"""
Написать функцию < season >, принимающую 1 аргумент — номер месяца (от 1 до 12),
и возвращающую время года, которому этот месяц принадлежит,
то есть: зима, весна, лето или осень.
"""


def season(mn: int):
    """
    :param mn: number of month
    :return: name of season to which this month belongs
    """
    if mn in [1, 2, 12]: return "зима"
    if mn in [3, 4, 5]: return "весна"
    if mn in [6, 7, 8]: return "лето"
    if mn in [9, 10, 11]: return "осень"
    return "error. month's number is incorrect"


months_number = int(input("Number of month: "))
print(season(months_number))
