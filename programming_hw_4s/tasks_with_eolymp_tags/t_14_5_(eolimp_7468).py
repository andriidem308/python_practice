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

    def reorder_list(self):
        if self.size < 3: return
        len_b = self.size // 2
        len_a = self.size - len_b

        self.this = self.head

        list_a = [self.this.data]
        list_b = []

        for _ in range(len_a-1):
            self.this = self.this.next
            list_a.append(self.this.data)
        for _ in range(len_b):
            self.this = self.this.next
            list_b.append(self.this.data)

        self.__init__()
        for i in range(len_a + len_b):
            if i % 2 == 0: self.add_to_tail(list_a[i // 2])
            else: self.add_to_tail(list_b[::-1][i // 2])

        pass

    def print(self):
        print(*self._damp())


n = int(input())
values = list(map(int, input().split()))
linked_list = List()

for v in values: linked_list.add_to_tail(v)

linked_list.reorder_list()
linked_list.print()
