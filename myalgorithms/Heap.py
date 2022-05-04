class Heap:
    def __init__(self):
        self.items = [0]
        self.size = 0

    def empty(self):
        return len(self.items) == 1

    def insert(self, *k):
        self.size += 1
        self.items.append(k[0])
        self.sift_up()

    def extract_minimum(self):
        root = self.items[1]
        self.items[1] = self.items[-1]

        self.items.pop()
        self.size -= 1

        self.sift_down()

        return root

    def sift_up(self):
        i = len(self.items) - 1

        while i > 1:
            parent = i // 2
            if self.items[i] < self.items[parent]:
                self.swap(parent, i)
            i = parent

    def sift_down(self):
        i = 1

        while 2*i <= self.size:
            left = 2*i
            right = 2*i + 1
            min_child = self.min_child(left, right)

            if self.items[i] > self.items[min_child]:
                self.swap(min_child, i)
            i = min_child

    def swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def min_child(self, left_child, right_child):
        if right_child > self.size: return left_child
        else:
            if self.items[left_child] < self.items[right_child]:
                return left_child
            else:
                return right_child


def heap_sort(array):
    size = len(array)

    for i in range(size // 2 - 1, -1, -1): sift_down(array, i, size)

    for i in range(size - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        sift_down(array, 0, i)


def sift_down(array, start, end):
    while True:
        left = start*2 + 1
        right = left + 1

        largest = start

        if left < end and array[left] > array[largest]:
            largest = left
        if right < end and array[right] > array[largest]:
            largest = right
        if largest == start:
            break

        array[start], array[largest] = array[largest], array[start]
        start = largest

