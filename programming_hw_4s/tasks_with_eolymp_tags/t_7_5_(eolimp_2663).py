def bubble_sort(array: list, length: int):
    has_swapped = True
    swapps = 0

    num_of_iterations = 0

    while has_swapped:
        has_swapped = False

        for i in range(length - num_of_iterations - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                has_swapped = True
                swapps += 1

        num_of_iterations += 1

    return swapps


n = int(input())
a = list(map(int, input().split()))

perms = bubble_sort(a, n)

print(perms)


