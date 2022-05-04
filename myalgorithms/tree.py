class Node:
    def __init__(self, key=None):
        self.key = key

    def empty(self): return self.key is None

    def set_key(self, key):
        self.key = key

    def get_key(self):
        return self.key


class Tree(Node):
    def __init__(self, key=None):
        super().__init__(key)
        self.children = []

    def empty(self):
        pass

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, key):
        for child in self.children:
            if child.data() == key:
                self.children.remove(child)
                return True
        return False

    def get_child(self, key):
        for child in self.children:
            if child.data == key:
                return child
        return None

    def get_children(self):
        return self.children


def create_sample_tree():
    node7 = Tree(7)
    node9 = Tree(9)
    node10 = Tree(10)
    node11 = Tree(11)
    node12 = Tree(12)
    node13 = Tree(13)
    node14 = Tree(14)
    node15 = Tree(15)

    node8 = Tree(8)
    node8.add_child(node14)
    node8.add_child(node15)
    node4 = Tree(8)
    node4.add_child(node8)
    node4.add_child(node9)
    node5 = Tree(8)
    node5.add_child(node10)
    node5.add_child(node11)
    node2 = Tree(2)
    node2.add_child(node4)
    node2.add_child(node5)

    node6 = Tree(6)
    node6.add_child(node12)
    node6.add_child(node13)
    node3 = Tree(3)
    node3.add_child(node6)
    node3.add_child(node7)

    root = Tree(1)
    root.add_child(node2)
    root.add_child(node3)