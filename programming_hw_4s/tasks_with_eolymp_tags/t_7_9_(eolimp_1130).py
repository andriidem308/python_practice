def insertion_sort(arr, length):
    for i in range(1, length):
        target = arr[i]

        j = i - 1
        while j >= 0 and arr[j] > target:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = target


def digits_sum(x):
    res = 0
    for c in str(x): res += int(c)

    return res


def get_position(arr, length, x):
    for p in range(length):
        if arr[p][1] == str(x):
            return p + 1


n = int(input())
k = int(input())

numbers = [(digits_sum(num), str(num)) for num in range(1, n+1)]
insertion_sort(numbers, n)

print(get_position(numbers, n, k), numbers[k - 1][1], sep='\n')


