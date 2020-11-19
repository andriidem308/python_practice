from SearchTree import SearchTree


class AVLTree(SearchTree):
    def __init__(self, key=None, left=None, right=None):
        super().__init__(key, left, right)
        self.balance_factor = 0
        self.is_root = False

    def set_left(self, item):
        if isinstance(item, AVLTree):
            self.left_child = item
        elif self.has_left():
            self.left_child.set_node(item)
        else:
            self.left_child = AVLTree(item)

        self.left_child.parent = self

    def set_right(self, item):
        if isinstance(item, AVLTree):
            self.right_child = item
        elif self.has_right():
            self.right_child.set_node(item)
        else:
            self.right_child = AVLTree(item)

        self.right_child.parent = self

    @staticmethod
    def rotate_left(node):
        node_parent = node.parent

        if node == node_parent.left_child:
            node_parent.left_child = AVLTree.__rotate_left(node)
        elif node == node_parent.right_child:
            node_parent.right_child = AVLTree.__rotate_left(node)

    @staticmethod
    def rotate_right(node):
        node_parent = node.parent

        if node == node_parent.left_child:
            node_parent.left_child = AVLTree.__rotate_right(node)
        elif node == node_parent.right_child:
            node_parent.right_child = AVLTree.__rotate_right(node)

    @staticmethod
    def __rotate_left(root):
        pivot = root.right_child
        root.right_child = pivot.left_child

        if pivot.left_child:
            pivot.left_child.parent = root
        pivot.left_child = root

        node_parent = root.parent
        root.parent = pivot
        pivot.parent = node_parent

        root.balance_factor = root.balance_factor + 1 - min(0, pivot.balance_factor)
        pivot.balance_factor = pivot.balance_factor + 1 + max(0, root.balance_factor)

        return pivot

    @staticmethod
    def __rotate_right(root):
        pivot = root.left_child
        root.left_child = pivot.right_child

        if pivot.right_child:
            pivot.right_child.parent = root
        pivot.right_child = root

        node_parent = root.parent
        root.parent = pivot
        pivot.parent = node_parent

        root.balance_factor = root.balance_factor - 1 - max(0, pivot.balance_factor)
        pivot.balance_factor = pivot.balance_factor - 1 + min(0, root.balance_factor)

        return pivot

    @staticmethod
    def rebalance(node):
        if node.balance_factor < 0:
            if node.right_child.balance_factor > 0:
                AVLTree.rotate_right(node.right_child)
                AVLTree.rotate_left(node)
            else:
                AVLTree.rotate_left(node)
        elif node.balance_factor > 0:
            if node.left_child.balance_factor < 0:
                AVLTree.rotate_left(node.left_child)
                AVLTree.rotate_right(node)
            else:
                AVLTree.rotate_right(node)

    @staticmethod
    def update_balance(node):
        if node.balance_factor > 1 or node.balance_factor < -1:
            AVLTree.rebalance(node)
            return

        if not node.parent.is_root:
            if node == node.parent.left_child:
                node.parent.balance_factor += 1
            elif node == node.parent.right_child:
                node.parent.balance_factor -= 1

            if node.parent.balance_factor != 0:
                AVLTree.update_balance(node.parent)

