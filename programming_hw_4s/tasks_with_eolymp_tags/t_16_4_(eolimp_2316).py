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

    def get_leaves(self):
        def _leaves(node):
            if node.has_left(): _leaves(node.get_left())
            if node.has_right(): _leaves(node.get_right())
            if not (node.has_left() or node.has_right()): leaves.append(node.get_key())

        leaves = []
        _leaves(self)

        return leaves


nodes = tuple(map(int, input().split()))

if nodes[0] == 0: pass
else:
    root = BinarySearchTree(nodes[0])
    nodes_amount = 1

    while nodes[nodes_amount] != 0:
        root.insert(nodes[nodes_amount])
        nodes_amount += 1

    print(*root.get_leaves())
