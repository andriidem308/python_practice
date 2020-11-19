class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class Stack:
    def __init__(self):
        self.top_node = None
        self.size = 0

    def empty(self):
        return self.top_node is None

    def push(self, value):
        self.size += 1
        new_node = Node(value)
        if not self.empty():
            new_node.next = self.top_node
        self.top_node = new_node
        return "ok"

    def pop(self):
        if self.empty(): return "error"
        self.size -= 1
        current_top = self.top_node
        item = current_top.item
        self.top_node = self.top_node.next
        del current_top
        return item

    def top(self):
        if self.empty(): return "error"
        return self.top_node.item

    def get_size(self):
        return self.size

    def clear(self):
        current_top = self.top_node
        if current_top is None: return
        while current_top:
            self.top_node = current_top.next
            current_top = self.top_node
            self.size -= 1
        return "ok"


new_stack = Stack()

while True:
    cmd = input().split()

    if cmd[0] == "push":
        new_stack.push(int(cmd[1]))
        print("ok")
    if cmd[0] == "pop":
        print(new_stack.pop())
    if cmd[0] == "back":
        print(new_stack.top())
    if cmd[0] == "size":
        print(new_stack.get_size())
    if cmd[0] == "clear":
        new_stack.clear()
        print("ok")
    if cmd[0] == "exit":
        print("bye")
        exit(0)

