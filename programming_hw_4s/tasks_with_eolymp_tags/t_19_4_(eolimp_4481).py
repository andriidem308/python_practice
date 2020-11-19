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

    def gcd(self,a,b):
        if (b == 0): return a
        else: return self.gcd(b, a % b)

    def get_gcd(self,l,r):
        return reduce(self.gcd, self.items[l:r + 1])


if __name__ == "__main__":
    with open("input.txt") as file_in:
        n = int(file_in.readline())
        arr = list(map(int, file_in.readline().split()))
        tree = SegmentTree(arr)
        m = int(file_in.readline())

        for i in range(m):
            q, l, r = (map(int, file_in.readline().split()))

            if q == 1: print(tree.get_gcd(l, r))
            elif q == 2: tree.update(l, r)
