"""
Написать функцию < is_prime >,
принимающую 1 аргумент — число от 0 до 1000,
и возвращающую < True >, если оно простое,
и < False > - иначе.
"""


def is_prime(n: int):
    if n in (2, 3): return True
    if n < 2 or n % 2 == 0 or n % 3 == 0: return False
    for i in range(5, int(n**(1/2)) + 1, 2):
        if n % i == 0: return False
    return True


number = int(input("Number for checking: "))
print("Is number prime? Answer:", is_prime(number))

