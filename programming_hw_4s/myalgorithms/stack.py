class Stack_:
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def top(self):
        if self.empty(): raise Exception("Stack: 'top' applied to empty container")

        return self.items[-1]

    def __len__(self):
        return len(self.items)
        
        
# -------------------------------------------------------------------------------------
        
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        

class Stack:
    def __init__(self):
        self.top_node = None
        
    def empty(self):
        return self.top_node is None
        
    def push(self, item):
        new_node = Node(item)
        if not self.empty(): 
            new_node.next = self.top_node
        
        self.top_node = new_node
        
    def pop(self):
        if self.empty(): raise Exception
        
        current_top = self.top_node
        item = current_top.item 
        
        self.top_node = self.top_node.next
        del current_top
        
        return item
    
    def top(self):
        if self.empty(): raise Exception
        
        return self.top_node.item
        
# =---------------------------------------------------------------------------------------
        
        
        
        