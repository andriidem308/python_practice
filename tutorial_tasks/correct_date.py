"""
Написать функцию < date >, принимающую 3 аргумента:
день, месяц и год.
Вернуть < True >, если такая дата есть в нашем календаре,
< False > - в противном случае.
"""
from tutorial_tasks.leap_year import is_year_leap


def date(d: str, m: str, y: str):
    if 2 < len(d) < 1: return False
    if 2 < len(m) < 1: return False
    if 4 < len(y) < 1: return False

    if int(d) not in tuple([i for i in range(1, 32)]): return False
    if int(m) not in tuple([i for i in range(1, 13)]): return False
    if int(y) not in tuple([i for i in range(10000)]): return False

    feb_d = 29 if is_year_leap(int(y)) else 28

    if int(m) in (4, 6, 9, 11) and int(d) == 31: return False
    if int(m) == 2 and int(d) > feb_d: return False

    return True


dmy_tup  = tuple(input("Enter date in format <dd.mm.yyyy> : ").split("."))
try:
    if len(dmy_tup) != 3: raise ValueError
    day, month, year = dmy_tup
    print("Is date correct? Answer:", date(day, month, year))
except ValueError:
    print("Invalid date format!")





