"""
Написать функцию < arithmetic >, принимающую 3 аргумента:
первые 2 - числа, третий - операция, которая должна быть произведена над ними.
Если третий аргумент:
    +, сложить их;
    —, то вычесть; (второе от первого)
    * — умножить;
    / — разделить (первое на второе).
В остальных случаях вернуть строку <<Неизвестная операция>>.
"""


def arithmetic(a: float, b: float, op: str):
    # c = a @ b, @ - operation
    if op == "+": c = a + b
    elif op == "-": c = a - b
    elif op == "*": c = a * b
    elif op == "/": c = a / b
    else: return "Unknown operation: <" + op + "> !!!"

    return int(c) if c == int(c) else c


number_1 = float(input("a: "))
number_2 = float(input("b: "))
operation = input("operation: ")

print("Result:", arithmetic(number_1, number_2, operation))
