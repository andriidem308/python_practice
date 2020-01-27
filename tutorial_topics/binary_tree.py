class Node:
    # initialize node (new tree)
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    # Insert method to create nodes
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # compare values with nodes
    def find(self, target):
        if target < self.data:
            if self.left is None:
                return str(target) + " NOT FOUND"
            return self.left.find(target)
        elif target > self.data:
            if self.right is None:
                return str(target) + " NOT FOUND"
            return self.right.find(target)
        else:
            return str(self.data) + " IS FOUND"

    # private - printing the tree but without '\n'
    def _print_tree(self):
        if self.left:
            self.left._print_tree()
        print(self.data, end=" ")
        if self.right:
            self.right._print_tree()
            # print()

    # public - printing the '\n' in addition
    def print_tree(self):
        self._print_tree()
        print()


if __name__ == "__main__":
    root = Node(12)
    print("Tree: ", end='')
    root.print_tree()

    # Nodes insertion
    root.insert(6)
    root.insert(14)
    root.insert(11)
    root.insert(1)
    root.insert(19)
    root.insert(3)
    root.insert(9)
    root.insert(9)

    # output tree after insertions
    print("Filled Tree: ", end='')
    root.print_tree()

    # tells if some elements found or not
    print("\nFINDING ELEMENTS:")
    print(root.find(12))
    print(root.find(3))
    print(root.find(4))
    print(root.find(8))
    print(root.find(6))
    print(root.find(7), '\n')

    # print("\n" + "-"*50 + "\n")

