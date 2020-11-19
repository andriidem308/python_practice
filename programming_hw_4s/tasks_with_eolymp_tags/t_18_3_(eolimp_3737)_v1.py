class Heap:
    def __init__(self):
        self.mItems = []
        self.mSize = 0

    def empty(self): return len(self.mItems) == 1

    def insert(self, element):
        self.mItems.append(element)
        self.mSize += 1

    def check_heap(self):
        if self.empty(): return False

        for p in range(self.mSize):
            condition_1 = (2 * p <= self.mSize and self.mItems[p] > self.mItems[2 * p])
            condition_2 = (2 * p + 1 <= n and self.mItems[p] > self.mItems[2 * p + 1])

            if condition_1 or condition_2:
                print("NO")
                return

        print("YES")


heap = Heap()
n = int(input())
lst = list(map(int, input().split()))

for i in range(len(lst)): heap.insert(lst[i])

heap.check_heap()

