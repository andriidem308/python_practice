class Queue:
    def __init__(self):
        self.queue = []

    def add(self, data):
        if data not in self.queue:
            self.queue.insert(0, data)
            return True
        return False

    def remove(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return "No elements in the queue"

    def size(self):
        return len(self.queue)