class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack[::-1])

    def push(self, value):
        if len(self.stack) < 100 and value >= 0:
            self.stack.append(value)
            print("ok")

    def pop(self):
        if len(self.stack) != 0:
            print(self.stack.pop())
        else:
            print("error")

    def back(self):
        if len(self.stack) != 0:
            print(self.stack[-1])
        else:
            print("error")

    def size(self):
        print(len(self.stack))

    def clear(self):
        self.stack = []
        print("ok")


new_stack = Stack()

while True:
    cmd = input().split()

    if cmd[0] == "push": new_stack.push(int(cmd[1]))
    if cmd[0] == "pop": new_stack.pop()
    if cmd[0] == "back": new_stack.back()
    if cmd[0] == "size": new_stack.size()
    if cmd[0] == "clear": new_stack.clear()
    if cmd[0] == "exit":
        print("bye")
        break