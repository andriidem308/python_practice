from math import log2, ceil


class SegmentTree:
    def __init__(self, array):
        k = len(array)
        amount = 1 << ceil(log2(k))
        self.items = amount * [0] + array + (amount - k) * [0]

        for i in range(k):
            self.items[i + 1] = array[i]

        self.size = amount

    def update(self, left, right, v):
        for i in range(left, right + 1):
            self.items[i] = v

    def eat(self, left, right):
        cnt = cnt_max = 1

        for i in range(left + 1, right + 1):
            if self.items[i - 1] <= self.items[i]:
                cnt += 1
            else:
                if cnt > cnt_max: cnt_max = cnt
                cnt = 1

        return cnt if cnt > cnt_max else cnt_max


if __name__ == "__main__":
    with open("input.txt") as file_in:
        with open("output.txt", "w") as file_out:
            n = int(file_in.readline())
            arr = list(map(int, file_in.readline().split()))
            tree = SegmentTree(arr)
            m = int(file_in.readline())

            for _ in range(m):
                arr = list(map(int, file_in.readline().split()))

                if arr[0] == 1: print(tree.eat(arr[1], arr[2]), file=file_out)
                elif arr[0] == 2: tree.update(arr[1], arr[2], arr[3])
