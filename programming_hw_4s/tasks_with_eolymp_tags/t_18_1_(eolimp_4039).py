class Heap:
    def __init__(self): self.items = [None]
    def __len__(self): return len(self.items) - 1
    def is_empty(self): return len(self) == 0
    def is_root(self, i): return i == 1
    def has_left(self, i): return i * 2 <= len(self)
    def has_right(self, i): return i * 2 + 1 <= len(self)
    def get_left(self, i): return i * 2
    def get_right(self, i): return i * 2 + 1
    def get_parent(self, i): return i // 2

    def insert(self, item):
        self.items.append(item)
        self.sift_up()

    def extract(self):
        if not self.is_empty():
            self.swap(1, -1)
            item = self.items.pop()
            self.sift_down()
            return item

    def swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def sift_up(self):
        current = len(self)

        while not self.is_root(current):
            parent = self.get_parent(current)

            if self.items[parent] < self.items[current]:
                self.swap(current, parent)
                current = parent
            else:
                break

    def sift_down(self):
        current = 1

        while self.has_left(current):
            child = self.get_max_child(current)

            if self.items[current] < self.items[child]:
                self.swap(current, child)
                current = child
            else:
                break

    def get_max_child(self, current):
        left = self.get_left(current)

        if self.has_right(current):
            right = self.get_right(current)

            if self.items[left] > self.items[right]: return left
            else: return right
        else:
            return left


heap = Heap()

n = int(input())

for _ in range(n):
    cmd = input().split()

    if cmd[0] == '0':
        item = int(cmd[1])
        heap.insert(item)
    elif cmd[0] == '1':
        print(heap.extract())
