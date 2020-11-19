def get_last(x):
    if x == 1: return 1
    if x % 2 == 0: return 2 * get_last(x / 2) - 1
    return 2 * get_last((x - 1) / 2) + 1


tests = int(input())
i = 0
while tests:
    tests -= 1

    n = int(input())
    r = 0
    k = get_last(n)
    while k != n:
        r += 1
        n = k
        k = get_last(n)

    i += 1
    print(f"Case {i}: {r} {n}")
