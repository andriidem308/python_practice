class PriorityQueue:
    def __init__(self):
        self.items = []
        
    def empty(self):
        return len(self.items) == 0
        
    def insert(self, priority, item):
        self.items.append((priority, item))
    
    def extract_minimum(self):
        if self.empty(): raise Exception
        
        minpos = 0
        for i in range(1, len(self.items)):
            if self.items[minpos][0] > self.items[i][0]:
                minpos = i
        
        return self.items.pop(minpos)[1]
    