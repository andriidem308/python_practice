def insertion_sort(arr, length):
    for ind in range(1, length):
        to_insert = arr[ind]
        j = ind - 1

        while j >= 0 and arr[j] > to_insert:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = to_insert


n = int(input())
times = [0] * n

for i in range(n):
    h, m, s = map(int, input().split())
    times[i] = h*3600 + m*60 + s

insertion_sort(times, n)

for time in times:
    h = time // 3600
    m = time % 3600 // 60
    s = time % 60

    print(h, m, s)

