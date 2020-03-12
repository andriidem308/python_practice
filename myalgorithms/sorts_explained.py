# Алгоритмы сортировки
# Sorting myalgorithms


# Check if arr is sorted
def check_sorted(arr: list, ascending:bool=True):
    """
    :param arr: list of elements
    :param ascending: True - from the lowest, False - from the highest
    :return: True if list is sorted, False - is not sorted
    """
    sign = 2 * int(ascending) - 1  # equal to 0 or -1
    for i in range(0, len(arr) - 1):
        if sign * arr[i] > sign * arr[i+1]: return False
    return True


# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
# Binary search of element in array
def binary_search(arr: list, element):
    """
    :param arr: list of sorted elements
    :param element: searching elements
    :return: tuple of left and right bounder
    """

    def _left_bound(arr, element):
        left = -1
        right = len(arr)
        while right - left > 1:
            middle = (left + right) // 2
            if arr[middle] < element: left = middle
            else:
                right = middle
        return left

    def _right_bound(arr, element):
        left = -1
        right = len(arr)
        while right - left > 1:
            middle = (left + right) // 2
            if arr[middle] <= element: left = middle
            else:
                right = middle
        return right

    return _left_bound(arr, element), _right_bound(arr, element)


# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
# Пузырьковая сортировка
# Bubble Sort

# Realization 1
def bubble_sort_1(arr: list):
    """
    :param arr: list of elements
    :return: sorted list
    """
    # Устанавливаем swapped в True, чтобы цикл запустился хотя бы один раз
    # Set swapped True for at least one loop realization
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                # Меняем элементы
                # Changing elements
                arr[i], arr[i+1] = arr[i+1], arr[i]
                # Устанавливаем swapped в True для следующей итерации
                # Set swapped True for next iteration
                swapped = True


# Realization 2
def bubble_sort_2(arr: list):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
# Сортировка выборкой
# Selection sort
def selection_sort(arr: list):
    # Значение i соответствует кол-ву отсортированных значений
    # Value of i equals to amount of sorted numbers
    for i in range(len(arr)):
        # Исходно считаем наименьшим первый элемент
        # Set first element as the minimum
        lowest_value_index = i
        # Этот цикл перебирает несортированные элементы
        # This loop look through unsorted elements
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[lowest_value_index]:
                lowest_value_index = j
        # Самый маленький элемент меняем с первым в списке
        # Swapping the lowest element with the first element
        arr[i], arr[lowest_value_index] = arr[lowest_value_index], arr[i]


# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
# Сортировка вставками
# Insertion sort
def insertion_sort(arr):
    # Сортировку начинаем со второго элемента,
    # т.к. считается, что первый элемент уже отсортирован
    # Begin sort with second element,
    # because we consider that first element has already sorted
    for i in range(1, len(arr)):
        item_to_insert = arr[i]
        # Сохраняем ссылку на индекс предыдущего элемента
        # Save the link of previous element's index
        j = i - 1
        # Элементы отсортированного сегмента перемещаем вперёд,
        # если они больше элемента для вставки
        # Elements of sorted segment move forward,
        # if they are bigger than insertion element
        while j >= 0 and arr[j] > item_to_insert:
            arr[j + 1] = arr[j]
            j -= 1
        # Вставляем элемент
        # Insert element
        arr[j + 1] = item_to_insert


# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
# Пирамидальная сортировка
# Heap Sort

def heap_sort(arr: list):
    def _heapify(arr: list, heap_size: int, root_index: int):
        # Индекс наибольшего элемента считаем корневым индексом
        largest = root_index
        left_child = (2 * root_index) + 1
        right_child = (2 * root_index) + 2

        # Если левый потомок корня — допустимый индекс, а элемент больше,
        # чем текущий наибольший, обновляем наибольший элемент
        if left_child < heap_size and arr[left_child] > arr[largest]:
            largest = left_child

        # То же самое для правого потомка корня
        if right_child < heap_size and arr[right_child] > arr[largest]:
            largest = right_child

        # Если наибольший элемент больше не корневой, они меняются местами
        if largest != root_index:
            arr[root_index], arr[largest] = arr[largest], arr[root_index]
            # Heapify the new root element to ensure it's the largest
            _heapify(arr, heap_size, largest)

    n = len(arr)

    # Создаём Max Heap из списка
    # Второй аргумент означает остановку алгоритма перед элементом -1, т.е.
    # перед первым элементом списка
    # 3-й аргумент означает повторный проход по списку в обратном направлении,
    # уменьшая счётчик i на 1
    for i in range(n, -1, -1):
        _heapify(arr, n, i)

    # Перемещаем корень Max Heap в конец списка
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        _heapify(arr, i, 0)


# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
# Сортировка слиянием
# Merge Sort

# Realisation 1
def merge_sort_1(arr: list):
    def _merge(left_list: list, right_list: list):
        _sorted_list = []
        i_left = i_right = 0
        # Длина списков часто используется, поэтому создадим переменные для удобства
        len_left, len_right = len(left_list), len(right_list)

        for _ in range(len_left + len_right):
            if i_left < len_left and i_right < len_right:
                # Сравниваем первые элементы в начале каждого списка
                # Если первый элемент левого подсписка меньше, добавляем его
                # в отсортированный массив
                if left_list[i_left] <= right_list[i_right]:
                    _sorted_list.append(left_list[i_left])
                    i_left += 1
                # Если первый элемент правого подсписка меньше, добавляем его
                # в отсортированный массив
                else:
                    _sorted_list.append(right_list[i_right])
                    i_right += 1

            # Если достигнут конец левого списка, элементы правого списка
            # добавляем в конец результирующего списка
            elif i_left == len_left:
                _sorted_list.append(right_list[i_right])
                i_right += 1
            # Если достигнут конец правого списка, элементы левого списка
            # добавляем в отсортированный массив
            elif i_right == len_right:
                _sorted_list.append(left_list[i_left])
                i_left += 1

        return _sorted_list

    # Возвращаем список, если он состоит из одного элемента
    if len(arr) <= 1: return arr

    # Для того чтобы найти середину списка, используем деление без остатка
    # Индексы должны быть integer
    i_middle = len(arr) // 2

    # Сортируем и объединяем подсписки
    left_list = arr[:i_middle]
    right_list = arr[i_middle:]
    merge_sort_1(left_list)
    merge_sort_1(right_list)

    # Объединяем отсортированные списки в результирующий
    sorted_list = _merge(left_list, right_list)
    for i in range(len(sorted_list)):
        arr[i] = sorted_list[i]


# Realisation 2
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


# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
# Сортировка Тони Хоарра (Быстрая сортировка)
# Toni Hoar's Sort (Quick sort)

# Realisation 1
def hoar_sort_1(arr: list):
    # Создадим вспомогательную функцию, которая вызывается рекурсивно
    def _partition(arr: list, low: int, high: int):
        # Выбираем средний элемент в качестве опорного
        # Также возможен выбор первого, последнего
        # или произвольного элементов в качестве опорного
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

            # Если элемент с индексом i (слева от опорного) больше, чем
            # элемент с индексом j (справа от опорного), меняем их местами
            arr[i], arr[j] = arr[j], arr[i]

    def _hoar_sort_1(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = _partition(items, low, high)
            _hoar_sort_1(items, low, split_index)
            _hoar_sort_1(items, split_index + 1, high)

    _hoar_sort_1(arr, 0, len(arr) - 1)


# Realisation 2
def hoar_sort_2(arr: list):
    if len(arr) <= 1: return
    barrier = arr[0]
    left_list = []
    right_list = []
    middle_list = []
    for x in arr:
        if x < barrier: left_list.append(x)
        elif x == barrier: middle_list.append(x)
        else: right_list.append(x)
    hoar_sort_2(left_list)
    hoar_sort_2(right_list)
    k = 0
    for x in left_list + middle_list + right_list:
        arr[k] = x
        k += 1


# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --