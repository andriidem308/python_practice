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


def DFS(tree: BinarySearchTree):
    print(tree.get_key(), end="")

    if tree.has_left(): DFS(tree.get_left())
    if tree.has_right(): DFS(tree.get_right())


deleted_nodes = ""

while True:
    line = input()
    if line == "*": break
    deleted_nodes += line

deleted_nodes = list(deleted_nodes)

if deleted_nodes:
    root = BinarySearchTree(deleted_nodes[-1])
    nodes_amount = len(deleted_nodes) - 1

    while nodes_amount >= 0:
        root.insert(deleted_nodes[nodes_amount])
        nodes_amount -= 1

    DFS(root)
