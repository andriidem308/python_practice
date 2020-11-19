class BinarySearchTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def get_key(self): return self.key
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


def DFS(tree, out=""):
    out += str(tree.get_key())
    print(tree.key, "->")
    if tree.has_left():

        DFS(tree.get_left(), out)
    if tree.has_right(): DFS(tree.get_right())
    return out


input(); tree_a = list(map(int, input().split()))
input(); tree_b = list(map(int, input().split()))

if tree_a:
    root_a = BinarySearchTree(tree_a[0])
    nodes_amount_a = 1

    while nodes_amount_a < len(tree_a):
        root_a.insert(tree_a[nodes_amount_a])
        nodes_amount_a += 1

if tree_b:
    root_b = BinarySearchTree(tree_b[0])
    nodes_amount_b = 1

    while nodes_amount_b < len(tree_b):
        root_b.insert(tree_b[nodes_amount_b])
        nodes_amount_b += 1

traversal_a = DFS(root_a)
traversal_b = DFS(root_b)

if traversal_a == traversal_b: print(1)
else: print(0)
