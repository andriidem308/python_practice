def combinations(arr, rep):
    if len(arr) <= rep:
        yield arr
        arr = []

    if arr:
        first = arr[0]
        rest = list(arr[1:])
        for comb in combinations(rest, rep - 1):
            yield [first] + comb
        for comb in combinations(rest, rep):
            yield comb


def permutations(arr):
    if len(arr) <= 1:
        yield arr
        arr = []

    for el in arr:
        rest = list(arr[:])
        rest.remove(el)
        for p in permutations(rest):
            yield [el] + p


def make_operation(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b


def calculate(x, y):
    if len(x) == 1:
        return x[0]

    return make_operation(calculate(x[:-1], y[:-1]), x[-1], y[-1])


def check_sequence(seq):
    for p in seq:
        for oc in OPCOMBINATIONS:
            tmp_res = calculate(p, oc)
            if tmp_res == 23:
                print(f"Possible")
                return
    print("Impossible")


OPERATIONS = ["+", "-", "*"] * 4
OPCOMBINATIONS = []

for opcomb in combinations(OPERATIONS, 4):
    if opcomb not in OPCOMBINATIONS:
        OPCOMBINATIONS.append(opcomb)

while True:
    number_array = list(map(int, input().split()))
    if number_array == [0] * 5: break

    NUMBERS = []
    for numperm in permutations(number_array):
        NUMBERS.append(numperm)

    check_sequence(NUMBERS)

