
class Tree:
    def __init__(self):
        self.children = {}

    def add_child(self, digit):
        self.children[digit] = Tree()

    def has_child(self, digit):
        return bool(self.children.get(digit))

    def get_child(self, digit):
        return self.children[digit]

    def has_children(self):
        return bool(self.children)

    def clear(self):
        self.children.clear()

    def add_phone(self, phone: str):
        node = self
        i = 0

        while i < len(phone) and node.has_child(phone[i]):
            node = node.get_child(phone[i])
            i += 1

        if i == len(phone): return False
        if i != 0 and not node.has_children(): return False

        while i < len(phone):
            node.add_child(phone[i])
            node = node.get_child(phone[i])
            i += 1

        return True


tree = Tree()
t = int(input())

for _ in range(t):
    ni = int(input())
    flag = True

    for __ in range(ni):
        phone = input().rstrip()
        if flag: flag = tree.add_phone(phone)

    print('YES' if flag else 'NO')
    tree.clear()
