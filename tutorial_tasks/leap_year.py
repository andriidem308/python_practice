"""
Написать функцию < is_year_leap >, принимающую 1 аргумент — год,
и возвращающую True, если год високосный, а False - в обратном случае.
"""


def is_year_leap(y: int):
    if y % 400 == 0: return True
    if y % 100 == 0: return False
    if y % 4 == 0: return True
    return False


if __name__ == "__main__":
    year = int(input("Year: "))
    print(is_year_leap(year))
