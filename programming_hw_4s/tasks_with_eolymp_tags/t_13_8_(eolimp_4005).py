MOVES_LIMIT = 2*10**5


class Queue:
    def __init__(self): self.queue = []

    def push(self, data):
        self.queue.insert(0, data)
        return "ok"

    def pop(self): return self.queue.pop()
    def front(self): return self.queue[-1]
    def size(self): return len(self.queue)

    def clear(self):
        self.queue = []
        return "ok"


first = Queue()
second = Queue()

n = int(input())
for e in input().split(): first.push(e)
for e in input().split(): second.push(e)
k = 0

while first.size() and second.size():
    k += 1

    a, b = first.pop(), second.pop()

    if (a > b) and ((b, a) != ('0', '9')) or ((a, b) == ('0', '9')):
        first.push(a)
        first.push(b)
    else:
        second.push(a)
        second.push(b)

    if k == MOVES_LIMIT:
        print('draw')
        break
else:
    print('first' if first.size() else 'second', k)
