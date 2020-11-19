def get_len(num): return len(str(num))


def multiply(x, y):
    len_x = get_len(x)
    len_y = get_len(y)

    len_max = max(len_x, len_y)

    if len_max < 10: return x * y

    len_max = len_max//2 + len_max%2

    multiplier = 10**len_max

    x1 = x // multiplier
    x0 = x - (x1*multiplier)
    y1 = y // multiplier
    y0 = y - (y1*multiplier)

    z0 = multiply(x0, y0)
    z1 = multiply(x0+x1, y0+y1)
    z2 = multiply(x1, y1)

    return z0 + ((z1 - z0 - z2) * multiplier) + (z2 * 10**(2*len_max))


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(multiply(a, b))