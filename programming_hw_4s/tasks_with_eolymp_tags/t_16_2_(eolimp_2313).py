class BinarySearchTree():
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

    def get_key(self): return self.data
    def has_left(self): return self.left is not None
    def has_right(self): return self.right is not None
    def get_left(self): return self.left
    def get_right(self): return self.right
    def set_left(self, key): self.left = BinarySearchTree(key)
    def set_right(self, key): self.right = BinarySearchTree(key)

    def insert(self, key):
        tmp_node = self

        while True:
            gotten_key = tmp_node.get_key()
            if key == gotten_key: break

            if key < gotten_key:
                if tmp_node.has_left(): tmp_node = tmp_node.get_left()
                else:
                    tmp_node.set_left(key)
                    break
            else:
                if tmp_node.has_right(): tmp_node = tmp_node.get_right()
                else:
                    tmp_node.set_right(key)
                    break

    def get_count(self):
        def _count(node):
            left_count = _count(node.get_left()) if node.has_left() else 0
            right_count = _count(node.get_right()) if node.has_right() else 0
            return left_count + right_count + 1
        return _count(self)


nodes = tuple(map(int, input().split()))

if nodes[0] == 0: print(0)
else:
    root = BinarySearchTree(nodes[0])
    nodes_amount = 1

    while nodes[nodes_amount] != 0:
        root.insert(nodes[nodes_amount])
        nodes_amount += 1

    print(root.get_count())

