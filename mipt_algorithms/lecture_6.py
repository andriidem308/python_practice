"""
    Here realized some algorithms:
    *   bubble_sort(array)
    *   insert_sort(array)
    *   selection_sort(array)
    *   count_sort(array)
"""


def bubble_sort(array):
    """Bubble sort"""
    n = len(array)
    for itr in range(1, n):
        for k in range(0, n-itr):
            if array[k] > array[k+1]:
                array[k], array[k+1] = array[k+1], array[k]


def insert_sort(array):
    """Insert sort"""
    n = len(array)
    for top in range(1, n):
        tmp_index = top
        while tmp_index > 0 and array[tmp_index-1] > array[tmp_index]:
            array[tmp_index], array[tmp_index-1] = array[tmp_index-1], array[tmp_index]
            tmp_index -= 1


def selection_sort(array):
    """Selection sort"""
    n = len(array)
    for pos in range(0, n-1):
        for k in range(pos+1, n):
            if array[k] < array[pos]:
                array[k], array[pos] = array[pos], array[k]


    pass


def count_sort(array: list):
    """Count sort"""
    max_value = max(array)
    values_counts = [0] * (max_value + 1)
    for tmp_val in array: values_counts[tmp_val] += 1
    array.clear()
    for value, repeats in enumerate(values_counts):
        array.extend([value] * repeats)


def test_sort(sort_algorithm):
    print("\nTesting:", sort_algorithm.__doc__)
    print("Test #1: ", end="")
    list_a = [4, 2, 5, 3, 1]
    list_a_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(list_a)
    print("Ok!" if list_a == list_a_sorted else "Fail!")

    print("Test #2: ", end="")
    list_b = list(range(10, 20)) + list(range(0, 10))
    list_b_sorted = list(range(0, 20))
    sort_algorithm(list_b)
    print("Ok!" if list_b == list_b_sorted else "Fail!")

    print("Test #3: ", end="")
    list_c = [6, 8, 2, 1, 4, 4, 5, 7, 6, 3]
    list_c_sorted = [1, 2, 3, 4, 4, 5, 6, 6, 7, 8]
    sort_algorithm(list_c)
    print("Ok!" if list_c == list_c_sorted else "Fail!")


if __name__ == "__main__":
    test_sort(bubble_sort)
    test_sort(insert_sort)
    test_sort(selection_sort)
    test_sort(count_sort)

