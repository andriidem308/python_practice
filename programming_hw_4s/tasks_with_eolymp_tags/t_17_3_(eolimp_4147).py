class AVLNode:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.balance = 0

    def has_left(self): return self.left is not None
    def has_right(self): return self.right is not None
    def has_no_children(self): return not (self.has_left() or self.has_right())
    def is_root(self): return isinstance(self.parent, AVLTree)
    def is_left(self): return self is self.parent.left
    def is_right(self): return self is self.parent.right
    def is_unbalanced(self): return abs(self.balance) > 1

    def set_left(self, key):
        self.left = AVLNode(key)
        self.left.parent = self
        self.left.update_balance()

    def set_right(self, key):
        self.right = AVLNode(key)
        self.right.parent = self
        self.right.update_balance()

    def update_balance(self):
        if self.is_unbalanced():
            return self.new_balance()
        if not self.is_root():
            parent = self.parent
            if self.is_left():
                parent.balance += 1
            elif self.is_right():
                parent.balance -= 1
            if parent.balance != 0:
                parent.update_balance()

    def new_balance(self):
        if self.balance < 0:
            if self.right.balance > 0:
                self.right.rotate_right()
                self.rotate_left()
            else:
                self.rotate_left()
        elif self.balance > 0:
            if self.left.balance < 0:
                self.left.rotate_left()
                self.rotate_right()
            else:
                self.rotate_right()

    def rotate_left(self):
        parent = self.parent
        if self.is_root():
            parent.root = self.__rotate_left()
        elif self.is_left():
            parent.left = self.__rotate_left()
        elif self.is_right():
            parent.right = self.__rotate_left()

    def __rotate_left(self):
        pivot = self.right
        self.right = pivot.left

        if pivot.has_left():
            pivot.left.parent = self
        pivot.left = self

        parent = self.parent
        self.parent = pivot
        pivot.parent = parent
        self.balance = self.balance + 1 - min(0, pivot.balance)
        pivot.balance = pivot.balance + 1 + max(0, self.balance)
        return pivot

    def rotate_right(self):
        parent = self.parent
        if self.is_root():
            parent.root = self.__rotate_right()
        elif self.is_left():
            parent.left = self.__rotate_right()
        elif self.is_right():
            parent.right = self.__rotate_right()

    def __rotate_right(self):
        pivot = self.left
        self.left = pivot.right

        if pivot.has_right():
            pivot.right.parent = self
        pivot.right = self

        parent = self.parent
        self.parent = pivot
        pivot.parent = parent

        self.balance = self.balance - 1 - max(0, pivot.balance)
        pivot.balance = pivot.balance - 1 + min(0, self.balance)
        return pivot

    def search(self, key):
        node = self
        while True:
            if key == node.key:
                return node
            elif key < node.key:
                if node.has_left():
                    node = node.left
                else:
                    break
            else:
                if node.has_right():
                    node = node.right
                else:
                    break

    def search_max(self):
        node = self
        while node.has_right():
            node = node.right
        return node

    def update_balance_on_delete(self, came_from_left):
        if came_from_left:
            self.balance -= 1
        else:
            self.balance += 1

        if self.is_unbalanced():
            self.new_balance()
            if not self.is_root():
                if self.parent.balance == 0 and not self.parent.is_root():
                    self.parent.parent.update_balance_on_delete(self.parent.is_left())
        elif self.balance == 0 and not self.is_root():
            self.parent.update_balance_on_delete(self.is_left())

    def delete(self, node_or_key):
        if isinstance(node_or_key, AVLNode):
            node = node_or_key
        else:
            node = self.search(node_or_key)
        if node is None:
            return

        parent = node.parent
        if node.has_no_children():
            if node.is_root():
                parent.root = None
            elif node.is_left():
                parent.left = None
                parent.update_balance_on_delete(True)
            elif node.is_right():
                parent.right = None
                parent.update_balance_on_delete(False)
        elif node.has_left() and not node.has_right():
            if node.is_root():
                parent.root = node.left
                node.left.parent = parent
            elif node.is_left():
                parent.left = node.left
                node.left.parent = parent
                parent.update_balance_on_delete(True)

            elif node.is_right():
                parent.right = node.left
                node.left.parent = parent
                parent.update_balance_on_delete(False)

        elif node.has_right() and not node.has_left():
            if node.is_root():
                parent.root = node.right
                node.right.parent = parent
            elif node.is_left():
                parent.left = node.right
                node.right.parent = parent
                parent.update_balance_on_delete(True)
            elif node.is_right():
                parent.right = node.right
                node.right.parent = parent
                parent.update_balance_on_delete(False)

        else:
            left_max = node.left.search_max()
            node.key = left_max.key
            node.left.delete(left_max)

    def exists(self, key):
        return bool(self.search(key))

    def insert(self, key):
        tmp_node = self

        while True:
            if key == tmp_node.key: break
            elif key < tmp_node.key:
                if tmp_node.has_left(): tmp_node = tmp_node.left
                else:
                    tmp_node.set_left(key)
                    break
            else:
                if tmp_node.has_right(): tmp_node = tmp_node.right
                else:
                    tmp_node.set_right(key)
                    break

    @staticmethod
    def next(tree, x):
        if tree is None or (tree.key == x and not tree.has_right()): return 'none'
        elif tree.key > x:
            k = AVLNode.next(tree.left, x)
            if k == 'none': return tree.key
            else: return k

        elif tree.key < x: return AVLNode.next(tree.right, x)
        elif tree.key == x: return AVLNode.next(tree.right, x)

    @staticmethod
    def prev(tree, x):
        if tree is None or (tree.key == x and not tree.has_left()): return 'none'
        elif tree.key < x:
            k = AVLNode.prev(tree.right, x)
            if k == 'none': return tree.key
            else: return k

        elif tree.key > x: return AVLNode.prev(tree.left, x)
        elif tree.key == x: return AVLNode.prev(tree.left, x)

    @staticmethod
    def kth(tree, ind, nodes_lst):
        if tree is None or nodes_lst[0] >= ind: return 'none'

        left = AVLNode.kth(tree.left, ind, nodes_lst)
        if left != 'none': return left

        nodes_lst[0] += 1
        if nodes_lst[0] == ind: return tree.key

        return AVLNode.kth(tree.right, ind, nodes_lst)


class AVLTree:
    def __init__(self): self.root = None

    def is_empty(self): return self.root is None

    def insert(self, key):
        if self.is_empty():
            self.root = AVLNode(key)
            self.root.parent = self
        else:
            self.root.insert(key)

    def exists(self, key):
        if self.is_empty(): return 'false'
        else: return 'true' if self.root.exists(key) else 'false'

    def delete(self, key):
        if not self.is_empty(): self.root.delete(key)

    def next(self, x):
        if not self.is_empty(): return AVLNode.next(self.root, x)
        else: return 'none'

    def prev(self, x):
        if not self.is_empty(): return AVLNode.prev(self.root, x)
        else: return 'none'

    def kth(self, i):
        if not self.is_empty(): return AVLNode.kth(self.root, i, [0])
        else: return 'none'


if __name__ == "__main__":
    root = AVLTree()

    while True:
        try: cmd, arg = input().split()
        except: break

        if cmd == 'insert': root.insert(int(arg))
        elif cmd == 'delete': root.delete(int(arg))
        elif cmd == 'exists': print(root.exists(int(arg)))
        elif cmd == 'next': print(root.next(int(arg)))
        elif cmd == 'prev': print(root.prev(int(arg)))
        elif cmd == 'kth': print(root.kth(int(arg)))