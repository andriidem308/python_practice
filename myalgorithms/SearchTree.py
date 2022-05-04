from BinaryTree import BinaryTree


class SearchTree(BinaryTree):
    def insert(self, key):
        self._insert_helper(self, key)

    def search(self, key):
        return self._search_helper(self, key)

    def delete(self, key):
        pass

    @staticmethod
    def _insert_helper(root, key):
        if root.key > key:
            if root.has_left():
                SearchTree._insert_helper(root.left_child, key)
            else:
                root.set_left(key)
        elif root.key < key:
            if root.has_right():
                SearchTree._insert_helper(root.right_child, key)
            else:
                root.set_right(key)

    @staticmethod
    def _search_helper(root, key):
        if root.key == key:
            return root
        elif key < root.key:
            if root.has_left():
                return SearchTree._search_helper(root.left_child, key)
            return None
        else:
            if root.has_right():
                return SearchTree._search_helper(root.right_child, key)
            return None

    @staticmethod
    def _search_max(root):
        if root.has_right():
            return SearchTree._search_max(root.right_child)
        else:
            return root

    @staticmethod
    def _delete_helper(root, key):
        node = SearchTree._search_helper(root, key)

        if node is None: return
        if node.has_no_children():
            if node.parent is None:
                node.key = None
            else:
                if node.parent.left_child == node:

                    node.parent.left_child = None
                else:
                    node.parent.right_child = None
        elif node.has_right() and not node.has_left():
            node.set_node(node.right_child)
        elif node.has_left() and not node.has_right():
            node.set_node(node.left_child)
        else:
            left_max = SearchTree._search_max(node.left_child)
            left_max_key = left_max.key

            node.set_node(left_max_key)
            SearchTree._delete_helper(node.left_child, left_max_key)
