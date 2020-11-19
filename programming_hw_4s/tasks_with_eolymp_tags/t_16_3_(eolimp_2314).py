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

    def second_maximum(self):
        tmp_node = self
        right_side = [tmp_node.get_key()]

        while tmp_node.has_right():
            tmp_node = tmp_node.get_right()
            right_side.append(tmp_node.get_key())

        right_side.pop()

        while True:
            if tmp_node.has_right():
                tmp_node = tmp_node.get_right()
                right_side.append(tmp_node.get_key())
            elif tmp_node.has_left():
                tmp_node = tmp_node.get_left()
                right_side.append(tmp_node.get_key())
            else:
                break
                
        return max(right_side)


nodes = tuple(map(int, input().split()))
root = BinarySearchTree(nodes[0])
nodes_amount = 1

while nodes[nodes_amount] != 0:
    root.insert(nodes[nodes_amount])
    nodes_amount += 1

print(root.second_maximum())
