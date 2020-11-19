class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack[::-1])

    def push(self, value):
        if len(self.stack) < 100:
            self.stack.append(value)
            print("ok")

    def pop(self):
        print(self.stack.pop())

    def back(self):
        print(self.stack[-1])

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