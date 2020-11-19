def insertion_sort(arr, length):
    for i in range(1, length):
        item_to_insert = arr[i]

        j = i - 1

        while j >= 0 and arr[j] > item_to_insert:
            arr[j + 1] = arr[j]
            j -= 1

        tmp = arr[:]
        arr[j + 1] = item_to_insert

        if tmp != arr:
            print(' '.join(map(str, arr)))


n = int(input())
a = list(map(int, input().split()))
insertion_sort(a, n)


