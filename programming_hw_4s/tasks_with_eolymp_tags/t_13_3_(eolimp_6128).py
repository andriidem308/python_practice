class Dequeue:
    def __init__(self): self.dequeue = []

    def push_front(self, data):
        self.dequeue.insert(0, data)
        return "ok"

    def push_back(self, data):
        self.dequeue.append(data)
        return "ok"

    def pop_front(self):
        tmp = self.dequeue[0]
        del self.dequeue[0]
        return tmp

    def pop_back(self):
        tmp = self.dequeue[-1]
        del self.dequeue[-1]
        return tmp

    def get_front(self): return self.dequeue[0]
    def get_back(self): return self.dequeue[-1]

    def get_size(self): return len(self.dequeue)

    def clear(self):
        self.dequeue = []
        return "ok"


new_dequeue = Dequeue()


def procedure(cmd):
    global new_dequeue
    if " " in cmd:
        cmd = cmd.split()
        if cmd[0] == "push_front": return new_dequeue.push_front(int(cmd[1]))
        if cmd[0] == "push_back": return new_dequeue.push_back(int(cmd[1]))
    if cmd == "pop_front": return new_dequeue.pop_front()
    if cmd == "pop_back": return new_dequeue.pop_back()
    if cmd == "front": return new_dequeue.get_front()
    if cmd == "back": return new_dequeue.get_back()
    if cmd == "size": return new_dequeue.get_size()
    if cmd == "clear": return new_dequeue.clear()


while True:
    command = input()
    if command == "exit":
        print("bye")
        break

    print(procedure(command))
