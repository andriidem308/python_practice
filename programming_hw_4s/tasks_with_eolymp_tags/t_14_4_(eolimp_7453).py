class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.this = None
        self.size = 0

    def add_to_tail(self, val):
        new_node = Node(val)

        if self.empty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.this

            if self.this.next:
                new_node.next = self.this.next
                new_node.next.prev = new_node
            else:
                self.tail = new_node

            new_node.prev.next = new_node

        self.this = self.tail

        self.size += 1

    def empty(self):
        return self.head is None

    def _damp(self):
        nodes = []
        current_node = self.head

        while current_node:
            nodes.append(current_node.data)
            current_node = current_node.next

        return nodes

    def rotate_right(self, x):
        if self.empty(): return
        if self.size == 1: return

        steps = x % self.size
        for _ in range(steps):
            tmp = self.tail
            tmp.next = self.head
            self.head.prev = tmp
            self.tail = self.tail.prev
            self.tail.next = None
            self.head = tmp

    def print(self):
        print(*self._damp())


n = int(input())
values = list(map(int, input().split()))
linked_list = List()

for v in values: linked_list.add_to_tail(v)

while True:
    try:
        k = int(input())
    except: break
    
    linked_list.rotate_right(k)
    linked_list.print()
