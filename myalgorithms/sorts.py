def check_sorted(arr: list, ascending: bool = True):
    sign = 2 * int(ascending) - 1

    for i in range(0, len(arr) - 1):
        if sign * arr[i] > sign * arr[i + 1]:
            return False

    return True


def binary_search(arr: list, element):
    def _left_bound():
        left = -1
        right = len(arr)

        while right - left > 1:
            middle = (left + right) // 2
            if arr[middle] < element:
                left = middle
            else:
                right = middle

        return left

    def _right_bound():
        left = -1
        right = len(arr)

        while right - left > 1:
            middle = (left + right) // 2
            if arr[middle] <= element:
                left = middle
            else:
                right = middle

        return right

    return _left_bound(), _right_bound()


def bubble_sort_1(arr: list):
    swapped = True

    while swapped:
        swapped = False

        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True


def bubble_sort_2(arr: list):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def selection_sort(arr: list):
    for i in range(len(arr)):
        lowest_value_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[lowest_value_index]:
                lowest_value_index = j

        arr[i], arr[lowest_value_index] = arr[lowest_value_index], arr[i]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        item_to_insert = arr[i]

        j = i - 1

        while j >= 0 and arr[j] > item_to_insert:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = item_to_insert


def heap_sort(arr: list):
    def _heapify(arr: list, heap_size: int, root_index: int):
        largest = root_index
        left_child = (2 * root_index) + 1
        right_child = (2 * root_index) + 2

        if left_child < heap_size and arr[left_child] > arr[largest]:
            largest = left_child

        if right_child < heap_size and arr[right_child] > arr[largest]:
            largest = right_child

        if largest != root_index:
            arr[root_index], arr[largest] = arr[largest], arr[root_index]
            _heapify(arr, heap_size, largest)

    n = len(arr)

    for i in range(n, -1, -1):
        _heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        _heapify(arr, i, 0)


def merge_sort_1(arr: list):
    def _merge(left_list: list, right_list: list):
        _sorted_list = []

        i_left = i_right = 0
        len_left, len_right = len(left_list), len(right_list)

        for _ in range(len_left + len_right):
            if i_left < len_left and i_right < len_right:
                if left_list[i_left] <= right_list[i_right]:
                    _sorted_list.append(left_list[i_left])
                    i_left += 1
                else:
                    _sorted_list.append(right_list[i_right])
                    i_right += 1

            elif i_left == len_left:
                _sorted_list.append(right_list[i_right])
                i_right += 1
            elif i_right == len_right:
                _sorted_list.append(left_list[i_left])
                i_left += 1

        return _sorted_list

    if len(arr) <= 1: return arr

    i_middle = len(arr) // 2

    left_list = arr[:i_middle]
    right_list = arr[i_middle:]

    merge_sort_1(left_list)
    merge_sort_1(right_list)

    sorted_list = _merge(left_list, right_list)
    for i in range(len(sorted_list)):
        arr[i] = sorted_list[i]


def merge_sort_2(arr: list):
    def _merge(left_arr: list, right_arr: list):
        _sorted_list = [0] * (len(left_arr) + len(right_arr))
        li = ri = 0
        n = 0
        while li < len(left_arr) and ri < len(right_arr):
            if left_arr[li] <= right_arr[ri]:
                _sorted_list[n] = left_arr[li]
                li += 1
                n += 1
            else:
                _sorted_list[n] = right_arr[ri]
                ri += 1
                n += 1
        while li < len(left_arr):
            _sorted_list[n] = left_arr[li]
            li += 1
            n += 1
        while ri < len(right_arr):
            _sorted_list[n] = right_arr[ri]
            ri += 1
            n += 1

        return _sorted_list

    if len(arr) <= 1: return

    middle = len(arr) // 2
    left = [arr[i] for i in range(0, middle)]
    right = [arr[i] for i in range(middle, len(arr))]

    merge_sort_2(left)
    merge_sort_2(right)

    central = _merge(left, right)

    for i in range(len(arr)):
        arr[i] = central[i]


def hoar_sort_1(arr: list):
    def _partition(arr: list, low: int, high: int):
        pivot = arr[(low + high) // 2]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while arr[i] < pivot:
                i += 1

            j -= 1
            while arr[j] > pivot:
                j -= 1

            if i >= j:
                return j

            arr[i], arr[j] = arr[j], arr[i]

    def _hoar_sort_1(items, low, high):
        if low < high:
            split_index = _partition(items, low, high)
            _hoar_sort_1(items, low, split_index)
            _hoar_sort_1(items, split_index + 1, high)

    _hoar_sort_1(arr, 0, len(arr) - 1)


def hoar_sort_2(arr: list):
    if len(arr) <= 1: return

    barrier = arr[0]

    left_list = []
    right_list = []
    middle_list = []

    for x in arr:
        if x < barrier:
            left_list.append(x)
        elif x == barrier:
            middle_list.append(x)
        else:
            right_list.append(x)

    hoar_sort_2(left_list)
    hoar_sort_2(right_list)

    k = 0

    for x in left_list + middle_list + right_list:
        arr[k] = x
        k += 1
