class SearchTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def get_key(self): 
        return self.key
    
    def has_left(self): 
        return self.left is not None
    
    def has_right(self): 
        return self.right is not None
    
    def get_left(self): 
        return self.left
    
    def get_right(self): 
        return self.right
    
    def set_left(self, key): 
        self.left = SearchTree(key)
    
    def set_right(self, key): 
        self.right = SearchTree(key)

    def insert(self, key):
        node = self
        while True: # Стандартна реалізація нерекурсивної вставки в дерево пошуку
            if key < node.get_key():
                if node.has_left():
                    node = node.get_left()
                else:
                    node.set_left(key)
                    break
            else:
                if node.has_right():
                    node = node.get_right()
                else:
                    node.set_right(key)
                    break

    def is_balanced(self):
        def _balanced(node):
            left_height = _balanced(node.get_left()) if node.has_left() else 0
            if left_height is False:
                return False # Якщо ліве піддерево незбалансоване, повертаємо False
            right_height = _balanced(node.get_right()) if node.has_right() else 0
            if right_height is False:
                return False # Якщо праве піддерево незбалансоване, повертаємо False
            if abs(left_height - right_height) > 1:
                return False # Якщо модуль різниці висот більше одиниці, повертаємо False
            return max(left_height, right_height) + 1
        return 1 if _balanced(self) else 0


if __name__ == '__main__':
    n = int(input())
    nodes = tuple(map(int, input().split()))
    root = SearchTree(nodes[0])
    for i in range(1, n):
        root.insert(nodes[i])
    print(root.is_balanced())