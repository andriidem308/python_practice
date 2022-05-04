class Deque:
    def __init__(self):
        self.items = []
        
    def empty(self):
        return len(self.items) == 0
        
    def append(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.empty(): raise Exception
        return self.items.pop()
        
    def append_left(self, item):
        self.items.insert(0, item)
    
    def pop_left(self):
        if self.empty(): raise Exception
        return self.items.pop(0)
    
    def __len__(self):
        return len(self.items)
    
# ----------------------------------------------------

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None
    
    
class Deque:
    def __init__(self):
        self.front = None
        self.back = None
        
    def empty(self):
        return self.front is None and self.back is None
        
    def append(self, item):
        new_node = Node(item)
        new_node.prev = self.back
        
        if not self.empty():
            self.back.next = new_node
        else:
            self.front = new_node
        
        self.back = new_node
    
    def pop(self):
        if self.empty(): raise Exception
        
        current_node = self.back
        item = current_node.item
        
        self.back = current_node.prev
        
        if self.back is None: self.front = None
        else: self.back.next = None
        
        del current_node
        return item
    
    def append_left(self, item):
        new_node = Node(item)
        new_node.next = self.front
        
        if not self.empty:
            self.front.prev = new_node
        else:
            self.back = new_node
        
        self.front = new_node
        
    def pop_left(self):
        if self.empty(): raise Exception
        
        current_node = self.front
        item = current_node.item
        self.front = current_node.next
        
        if self.front is None:
            self.back = None
        else:
            self.front.prev = None
            
        del current_node
        
        return item
        
    def __del__(self):
        while self.front is not None:
            current_node = self.front
            self.front = self.front.next
            del current_node
        
        self.back = None
        
        
        
        
        
        
        
        
        
        
        
        
            
        
        
        
        
        