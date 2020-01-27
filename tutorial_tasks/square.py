"""
Написать функцию < square >, принимающую 1 аргумент — сторону квадрата,
и возвращающую 3 значения (с помощью кортежа):
    периметр квадрата,
    площадь квадрата
    и диагональ квадрата.
"""


def square(s: float):
    p = s * 4
    a = s * s
    d = s * 2 ** (1 / 2)
    return p, a, d


side = float(input("Square side: "))
perimeter, area, diagonal = square(side)

print("\nPerimeter:", perimeter)
print("Area:", area)
print("Diagonal:", round(diagonal, 3))
