from Vertex import Vertex


class Graph:
    def __init__(self, directed=False):
        self.is_directed = directed
        self.vertex_number = 0
        self.vertices = {}
        
    def add_vertex(self, vertex):
        if vertex in self: return False
        
        new_vertex = Vertex(vertex)
        self.vertices[vertex] = new_vertex
        self.vertex_number += 1
        return True

    def get_vertex(self, vertex):
        assert vertex in self

        key = vertex.key() if isinstance(vertex, Vertex) else vertex
        return self.vertices[key]

    def vertices(self):
        return self.vertices

    def add_edge(self, source, destination, weight=1):
        if source not in self: self.add_vertex(source)
        if destination not in self: self.add_vertex(destination)

        self[source].add_neighbour(destination, weight)

        if not self.is_directed:
            self.vertices[destination].add_neighbour(source, weight)

    def set_data(self, vertex, data):
        assert vertex in self
        self[vertex].set_data(data)

    def get_data(self, vertex):
        assert vertex in self
        return self[vertex].data()

    def transpose(self):
        g_inv = Graph(self.is_directed)

        for vertex in self:
            for neighbour_key in vertex.neighbours():
                g_inv.add_edge(neighbour_key, vertex.key())

        return g_inv

    def __contains__(self, vertex):
        if isinstance(vertex, Vertex):
            return vertex.key() in self.vertices
        else:
            return vertex in self.vertices

    def __iter__(self):
        return iter(self.vertices.values())

    def __len__(self):
        return self.vertex_number

    def __getitem__(self, vertex):
        return self.get_vertex(vertex)

