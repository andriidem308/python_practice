def merge_sort(arr: list):
    def merge(left, right):
        length_l, length_r = len(left), len(right)
        index_l = index_c = index_r = 0

        sorted_arr = [0] * (length_l + length_r)

        while index_l < length_l and index_r < length_r:
            if left[index_l][0] == right[index_r][0]:
                if left[index_l][1] <= right[index_r][1]:
                    sorted_arr[index_c] = left[index_l]
                    index_l += 1
                    index_c += 1
                else:
                    sorted_arr[index_c] = right[index_r]
                    index_r += 1
                    index_c += 1
            elif left[index_l][0] < right[index_r][0]:
                sorted_arr[index_c] = left[index_l]
                index_l += 1
                index_c += 1
            else:
                sorted_arr[index_c] = right[index_r]
                index_r += 1
                index_c += 1

        while index_l < length_l:
            sorted_arr[index_c] = left[index_l]
            index_l += 1
            index_c += 1

        while index_r < length_r:
            sorted_arr[index_c] = right[index_r]
            index_r += 1
            index_c += 1

        return sorted_arr

    if len(arr) <= 1: return

    middle = len(arr) // 2
    left_arr = arr[:middle]
    right_arr = arr[middle:]

    merge_sort(left_arr)
    merge_sort(right_arr)

    central = merge(left_arr, right_arr)

    for i in range(len(arr)):
        arr[i] = central[i]


n = int(input())
lines = [tuple()] * n

for i in range(n):
    lines[i] = tuple(map(int, input().split()))

merge_sort(lines)
for line in lines:
    print(line[0], line[1], sep=' ')