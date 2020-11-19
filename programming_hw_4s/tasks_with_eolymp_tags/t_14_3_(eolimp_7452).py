class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.this = None

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

        # self.size += 1

    def empty(self):
        return self.head is None

    def _damp(self):
        nodes = []
        current_node = self.head

        while current_node:
            nodes.append(current_node.data)
            current_node = current_node.next

        return nodes

    def print(self):
        print(*self._damp())

    def print_reverse(self):
        print(*(self._damp()[::-1]))


n = int(input())
values = list(map(int, input().split()))
linked_list = List()

for v in values: linked_list.add_to_tail(v)

linked_list.print()
linked_list.print_reverse()
