class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedQueue:
    def __init__(self):
        self.front = None
        self.size = 0

    def push(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.front = new_node
        else:
            tmp = self.front
            while tmp.next is not None: tmp = tmp.next
            tmp.next = new_node
            del tmp

        self.size += 1
        return "ok"

    def pop(self):
        if self.is_empty(): return "error"
        front = self.front.data
        self.front = self.front.next
        self.size -= 1
        return front

    def get_front(self):
        if self.is_empty(): return "error"
        return self.front.data

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.front is None

    def clear(self):
        if self.front:
            self.front = None
            self.size = 0
        return "ok"


new_linked_queue = LinkedQueue()


def procedure(cmd):
    global new_linked_queue

    if " " in cmd: return new_linked_queue.push(int(cmd.split()[1]))
    if cmd == "pop": return new_linked_queue.pop()
    if cmd == "front": return new_linked_queue.get_front()
    if cmd == "size": return new_linked_queue.get_size()
    if cmd == "clear": return new_linked_queue.clear()
    return ""


while True:
    command = input()
    if command == "exit":
        print("bye")
        break

    print(procedure(command))
