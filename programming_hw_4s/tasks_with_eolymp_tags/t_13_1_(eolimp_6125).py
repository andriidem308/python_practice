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


new_queue = Queue()


def procedure(cmd):
    global new_queue
    if " " in cmd: return new_queue.push(int(cmd.split()[1]))
    if cmd == "pop": return new_queue.pop()
    if cmd == "front": return new_queue.front()
    if cmd == "size": return new_queue.size()
    if cmd == "clear": return new_queue.clear()


while True:
    command = input()
    if command == "exit":
        print("bye")
        break

    print(procedure(command))
