class VertexBase:
    def __init__(self, key):
        self.key = key
        self.data = None

    def key(self):
        return self.key

    def set_data(self, data):
        self.data = data

    def data(self):
        return self.data

