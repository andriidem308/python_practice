class Stack:
    def __init__(self):
        self.stack = []
        self.answer = ''

    def fill(self, a, p):
        while a > 0:
            self.stack.append(a % p)
            a //= p

    def output(self):
        while self.stack:
            el = self.stack.pop()

            if el <= 9:
                self.answer += str(el)
            else:
                self.answer += f"[{el}]"

        return self.answer


a = int(input())
p = int(input())

obj = Stack()
obj.fill(a, p)

print(obj.output())
