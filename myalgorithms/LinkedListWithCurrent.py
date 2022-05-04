class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        

class ListWithCurrent:
    def __init__(self):
        self.head = None
        self.current = None
    
    def empty(self):
        return self.head is None
    
    def reset(self):
        self.current = self.head
    
    def next(self):
        if self.empty():
            raise Exception
        else:
            self.current = self.current.next
        
    def current(self):
        if self.empty():
            return None
        else:
            return self.current.item
            
    def insert(self, item):
        new_node = Node(item)
        
        if self.empty():
            self.head = new_node
            self.current = new_node
        else:
            new_node.next = self.current.next
            self.current.next = new_node
    
    def __str__(self):
        return str(self.current())
        
     