def quick_sort(arr, a, b):
    if a >= b: return

    pivot = arr[(a+b)//2]
    left = a
    right = b

    while True:
        while arr[left] < pivot: left += 1
        while pivot < arr[right]: right -= 1

        if left >= right: break

        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    quick_sort(arr, a, right)
    quick_sort(arr, right + 1, b)


if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))

    quick_sort(array, 0, n-1)

    for el in array:
        print(el, end=' ')

