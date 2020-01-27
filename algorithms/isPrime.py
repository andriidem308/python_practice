def is_prime(n):
    if n in (2, 3): return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n ** 0.5) + 1, 2):  # only odd numbers
        if n % i == 0:
            return False

    return True


def get_digit_sum(number):
    res = 0
    while number > 0:
        res += number % 10
        number //= 10
    return res


k = 0
for i in range(1000, 10000):
    if is_prime(i) and is_prime(get_digit_sum(i)):
        k += 1

print(k)
