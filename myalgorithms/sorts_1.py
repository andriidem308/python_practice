def bubble_sort(arr):
    swapped = True

    while swapped:
        swapped = False

        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True


def selection_sort(arr):
    for i in range(len(arr)):
        minpos = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minpos]:
                minpos = j

        arr[i], arr[minpos] = arr[minpos], arr[i]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = current


def merge_sort(array):
    def _merge(left_arr, right_arr):
        _summary = [0] * (len(left_arr) + len(right_arr))
        li = ri = n = 0

        while li < len(left_arr) and ri < len(right_arr):
            if left_arr[li] <= right_arr[ri]:
                _summary[n] = left_arr[li]
                li += 1
                n += 1
            else:
                _summary[n] = right_arr[ri]
                ri += 1
                n += 1

        while li < len(left_arr):
            _summary[n] = left_arr[li]
            li += 1
            n += 1

        while ri < len(right_arr):
            _summary[n] = right_arr[ri]
            ri += 1
            n += 1

        return _summary

    if len(array) <= 1: return

    middle = len(array) // 2
    left_array = [array[i] for i in range(0, middle)]
    right_array = [array[i] for i in range(middle, len(array))]

    merge_sort(left_array)
    merge_sort(right_array)

    summary = _merge(left_array, right_array)

    for i in range(len(array)):
        array[i] = summary[i]


def quick_sort(array):
    if len(array) <= 1:
        return

    pivot = array[0]

    left_array = []
    right_array = []
    middle_array = []

    for x in array:
        if x < pivot:
            left_array.append(x)
        elif x > pivot:
            right_array.append(x)
        else:
            middle_array.append(x)

    quick_sort(left_array)
    quick_sort(right_array)

    index = 0

    for x in left_array + middle_array + right_array:
        array[index] = x
        index += 1
