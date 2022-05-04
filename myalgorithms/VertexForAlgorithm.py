from Vertex import Vertex
INF = 10**9


class VertexForAlgorithms(Vertex):
    def __init__(self, key):
        super().__init__(key)
        self.distance = INF
        self.source = None

    def set_distance(self, distance):
        self.distance = distance

    def distance(self):
        return self.distance

    def set_source(self, source):
        self.source = source

    def source(self):
        return self.source