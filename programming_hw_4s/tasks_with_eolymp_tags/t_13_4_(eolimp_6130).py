class Node:

    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class LinkedDequeue:

    def __init__(self):
        self._front = None
        self._back = None
        self._len = 0

    def push_front(self, item):
        node = Node(item)
        if self._front:
            self._front.prev = node
            node.next = self._front
        else:
            self._back = node
        self._front = node
        self._len += 1
        return 'ok'

    def push_back(self, item):
        node = Node(item)
        if self._back:
            self._back.next = node
            node.prev = self._back
        else:
            self._front = node
        self._back = node
        self._len += 1
        return 'ok'

    def pop_front(self):
        if self._front:
            node = self._front
            self._front = node.next
            if self._front:
                self._front.prev = None
            else:
                self._back = None
            self._len -= 1
            return node.item
        return 'error'

    def pop_back(self):
        if self._back:
            node = self._back
            self._back = node.prev
            if self._back:
                self._back.next = None
            else:
                self._front = None
            self._len -= 1
            return node.item
        return 'error'

    def front(self):
        return self._front.item if self._front else 'error'

    def back(self):
        return self._back.item if self._back else 'error'

    def size(self):
        return self._len

    def clear(self):
        self.__init__()
        return 'ok'

    def exit(self):
        return 'bye'

    def execute(self, command):
        command = command.split()
        name = command[0]
        args = command[1:]
        return getattr(self, name)(*args)


if __name__ == '__main__':
    new_linked_deque = LinkedDequeue()

    with open('input.txt') as input:
        with open('output.txt', 'w') as output:
            for line in input:
                result = new_linked_deque.execute(line.rstrip())
                print(result, file=output)
                
                if result == 'bye': break