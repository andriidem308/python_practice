from VertexBase import VertexBase


class Vertex(VertexBase):
    def __init__(self, key):
        super().__init__(key)
        self.neighbours = {}

    def add_neighbour(self, vertex, weight=1):
        if isinstance(vertex, VertexBase):
            self.neighbours[vertex.key()] = weight
        else:
            self.neighbours[vertex] = weight

    def neighbours(self):
        return self.neighbours.keys()

    def weight(self, neighbour):
        if isinstance(neighbour, VertexBase):
            return self.neighbours[neighbour.key()]
        else:
            return self.neighbours[neighbour]
    