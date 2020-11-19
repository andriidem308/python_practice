from math import log2, ceil


class SegmentTree:
    def __init__(self, array):
        k = len(array)
        amount = 1 << ceil(log2(k))
        self.items = amount * [0] + array + (amount - k) * [0]

        for i in range(amount - 1, 0, -1):
            self.items[i] = self.items[i * 2] + self.items[i * 2 + 1]

        self.size = amount

    def plus(self, i, item):
        i += self.size
        self.items[i] += item

        while i != 1:
            i = i // 2
            self.items[i] = self.items[i * 2] + self.items[i * 2 + 1]

    def sum(self, left, right):
        left += self.size
        right += self.size
        result = 0

        while left <= right:
            if left % 2 == 1: result += self.items[left]
            if right % 2 == 0: result += self.items[right]

            left = (left + 1) // 2
            right = (right - 1) // 2

        return result


if __name__ == "__main__":
    with open('input.txt') as file_in:
        n, q = map(int, file_in.readline().split())
        arr = list(map(int, file_in.readline().split()))
        tree = SegmentTree(arr)

        for _ in range(q):
            cmd = file_in.readline().split()

            if cmd[0] == '+': tree.plus(int(cmd[1]) - 1, int(cmd[2]))
            elif cmd[0] == '?': print(tree.sum(int(cmd[1]) - 1, int(cmd[2]) - 1))
