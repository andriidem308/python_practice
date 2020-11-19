RESULT = 0


def calculate(arr, flag):
    global RESULT

    if len(arr) == 0: return

    if flag: RESULT += max(arr[0], arr[1])
    else: RESULT += min(arr[0], arr[1])

    calculate(arr[2:], not flag)


n = int(input())
weights = list(map(int, input().split()))

calculate(weights[::-1], True)
print(RESULT)

