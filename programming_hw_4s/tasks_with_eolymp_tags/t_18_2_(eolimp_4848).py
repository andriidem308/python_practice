def heap_sort(array: list):
    def _heapify(_array: list, heap_size: int, root_index: int):
        largest = root_index
        left_child = (2 * root_index) + 1
        right_child = (2 * root_index) + 2

        if left_child < heap_size and _array[left_child] > _array[largest]:
            largest = left_child

        if right_child < heap_size and _array[right_child] > _array[largest]:
            largest = right_child

        if largest != root_index:
            _array[root_index], _array[largest] = _array[largest], _array[root_index]
            _heapify(_array, heap_size, largest)

    n = len(array)

    for i in range(n, -1, -1):
        _heapify(array, n, i)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        _heapify(array, i, 0)


arr = list(map(int, input().split()))
heap_sort(arr)
print(*arr)

