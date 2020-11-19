class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.first = None
    
    def empty(self):
        return self.first is None
    
    def insert(self, item):
        new_node = Node(item)
        new_node.next = self.first
        self.first = new_node
        
    def head(self):
        if self.empty():
            return None
        else:
            return self.first.item
    
    def tail(self):
        if self.empty():
            raise Exception
        
        self.first = self.first.next
        return self
        