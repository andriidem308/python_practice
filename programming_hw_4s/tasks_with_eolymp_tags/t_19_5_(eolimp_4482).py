from math import log2, ceil
from functools import reduce


class SegmentTree:
    def __init__(self, array):
        k = len(array)
        amount = 1 << ceil(log2(k))
        self.items = amount * [0] + array + (amount - k) * [0]

        for i in range(len(array)):
            self.items[i + 1] = array[i]

        self.size = amount

    def update(self, pos, x):
        self.items[pos] = x

    def get_max(self, left, right):
        return max(self.items[left:right + 1])

    def get_min(self, left, right):
        return min(self.items[left:right + 1])


if __name__ == "__main__":
    with open("input.txt") as file_in:
        n = int(file_in.readline())
        arr = list(map(int, file_in.readline().split()))
        tree = SegmentTree(arr)
        m = int(file_in.readline())

        for i in range(m):
            q, l, r = (map(int, file_in.readline().split()))

            if q == 1:
                tree_min = tree.get_min(l, r)
                tree_max = tree.get_max(l, r)
                print("draw" if tree_min == tree_max else "wins")
            elif q == 2:
                tree.update(l, r)
