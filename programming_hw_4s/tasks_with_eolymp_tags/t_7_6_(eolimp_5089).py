def merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2
        lefthalf = arr[:middle]
        righthalf = arr[middle:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = j = k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]
                i += 1
            else:
                arr[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            arr[k] = righthalf[j]
            j += 1
            k += 1


def insertion_sort(arr, length):
    for i in range(1, length):
        item_to_insert = arr[i]

        j = i - 1

        while j >= 0 and arr[j] > item_to_insert:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = item_to_insert


n = int(input())
words = [''] * n

for i in range(n):
    words[i] = input()

# merge_sort(words)
insertion_sort(words, n)

for w in words:
    print(w)

