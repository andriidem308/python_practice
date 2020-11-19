class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack[::-1])

    def size(self):
        return len(self.stack)

    def clear(self):
        self.stack = []

    def push(self, value):
        if len(self.stack) < 100 and value >= 0: self.stack.append(value)

    def pop(self):
        if len(self.stack) != 0:
            return self.stack.pop()
        else:
            print("error")

    def back(self):
        if len(self.stack) != 0:
            return self.stack[-1]
        else:
            print("error")


if __name__ == "__main__":
    while True:
        try:
            n = int(input())
            if n == 0: break
        except:
            exit(0)

        while True:
            target = [0] + list(map(int, input().split()))
            if target[1] == 0: break
            s = Stack()

            ok = True
            A = 1
            B = 1

            while B <= n:
                if A == target[B]:
                    A += 1
                    B += 1
                elif s.size() and s.back() == target[B]:
                    s.pop()
                    B += 1
                elif A <= n:
                    s.push(A)
                    A += 1
                else:
                    ok = False
                    break
            print("Yes" if ok else "No")
        print()
