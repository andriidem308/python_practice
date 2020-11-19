# ----- Sorting myalgorithms given by teacher -----

# Here will be realized a list of these sorts:
#       * Bubble sort
#       * Selection sort
#       * Insertion sort
#       * Merge sort
#       * Quick sort


# ** BUBBLE SORT **
def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# ** SELECTION SORT **
def selection_sort(arr):
    n = len(arr)
    max_pos = 0

    for i in range(n - 1, 0, -1):
        for j in range(1, i + 1):
            if arr[max_pos] < arr[j]:
                max_pos = j
        arr[i], arr[max_pos] = arr[max_pos], arr[i]


# ** INSERTION SORT **
def insertion_sort(arr):
    n = len(arr)

    for index in range(1, n):
        current_value = arr[index]
        position = index

        while position > 0:
            if arr[position - 1] > current_value:
                arr[position] = arr[position - 1]
            else:
                break
            position -= 1

        arr[position] = current_value


# ** MERGE SORT **
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


# ** QUICK SORT **
def qsort(arr, a, b):
    if a >= b: return

    pivot = arr[(a+b)//2]
    left = a
    right = b

    while True:
        while arr[left] < pivot:
            left += 1

        while pivot < arr[right]:
            right -= 1

        if left >= right:
            break

        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    qsort(arr, a, right)
    qsort(arr, right + 1, b)


