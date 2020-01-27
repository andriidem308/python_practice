# tasks 1-55


# task 1
# Write a Python program to check
# if a given positive integer is a power of two
def check_power_of_2(num):
    if num == 1: return True
    while num > 0:
        if num == 2: return True
        num /= 2
    return False


# task 2
# Write a Python program to check
# if a given positive integer is a power of three
def check_power_of_3(num):
    if num == 1: return True
    while num > 0:
        if num == 3: return True
        num /= 3
    return False


# task 18
# Write a Python program to reverse the digits of an integer.
def reverse_number(num):
    if str(num)[0] == '-':

        return -1 * int(str(num)[-1:0:-1])
    return int(str(num)[::-1])


# task 19
# Write a Python program to reverse the bits of an integer (32 bits unsigned)
def reverse_bits(num: int):
    bits_list = [b for b in str(bin(num))[2:]]
    res = 0
    for i, e in enumerate(bits_list): res += int(e) * 2**i
    return res


# task 20
# Write a Python program to check a sequence of numbers
# is an arithmetic progression or not
def is_arithmetic_progression(some_lst):
    d = some_lst[1] - some_lst[0]
    for i in range(1, len(some_lst)):
        if some_lst[i] - some_lst[i-1] != d: return False
    return True


# task 21
# Write a Python program to check a sequence of
# numbers is a geometric progression or not.
def is_geometric_progression(some_lst):
    q = some_lst[1] / some_lst[0]
    for i in range(1, len(some_lst)):
        if some_lst[i] / some_lst[i-1] != q: return False
    return True


# task 22
# Write a Python program to compute the sum of the
# two reversed numbers and display the sum in reversed form.
def reversed_sum(a, b):
    return str(int(str(a)[::-1]) + int(str(b)[::-1]))[::-1]


# task 23
# Write a Python program to check whether a given number is an ugly number.
def is_ugly(num):
    if num == 0:
        return False
    for i in [2, 3, 5]:
        while num % i == 0:
            num /= i
    return num == 1
