class Queue:
    def __init__(self):
        self.items = []
        
    def empty(self):
        return len(self.items) == 0
        
    def enqueue(self, item):
        """ Додає елемент у чергу """
        self.items.append(item)
    
    def dequeue(self):
        """ """
        if self.empty(): raise Exception
        return self.items.pop(0)
    
    def __len__(self):
        return len(self.items)
        
# ---------------------------------------------------

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
    
    
class Queue:
    def __init__(self):
        self.front = None
        self.back = None
    
    def empty(self):
        return self.front is None and self.back is None
    
    def enqueue(self, item):
        new_node = Node(item)
        
        if self.empty():
            self.front = new_node
        else:
            self.back.next = new_node
        
        self.back = new_node
    
    def dequeue(self):
        if self.empty(): raise Exception
        
        current_front = self.front
        item = current_front.item
        
        self.front = self.front.next
        del current_front
        
        if self.front is None: self.back = None
        return item
        
    