from Queue import Queue


class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_child = None
        self.parent = None
        
    def has_left(self):
        return self.left_child is not None
    
    def has_right(self):
        return self.right_child is not None
        
    def has_no_children(self):
        return self.left_child is None and self.right_child
    
    def set_node(self, item):
        if isinstance(item, BinaryTree):
            self.key = item.key
            self.left_child = item.left_child
            self.right_child = item.right_child
        else:
            self.key = item
            
    def set_left(self, item):
        if isinstance(item, BinaryTree):
            self.left_child = item
        elif self.has_left():
            self.left_child.set_node(item)
        else:
            self.left_child = BinaryTree(item)
            
        self.left_child.parent = self
            
    def set_right(self, item):
        if isinstance(item, BinaryTree):
            self.right_child = item
        elif self.has_right():
            self.right_child.set_node(item)
        else:
            self.right_child = BinaryTree(item)
            
        self.right_child.parent = self
        
    def remove_left(self):
        self.left_child = None
        
    def remove_right(self):
        self.right_child = None
        
    




def DFS(root):
    print(root.key)
    
    if root.has_left(): DFS(root.left_child)
    if root.has_right(): DFS(root.right_child)

    
def BFS(root):
    q = Queue() 