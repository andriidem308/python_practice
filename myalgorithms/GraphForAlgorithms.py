from VertexForAlgorithm import VertexForAlgorithms, INF
from Graph import Graph
from Stack import Stack


class GraphForAlgorithms(Graph):
    def add_vertex(self, vertex):
        if vertex in self: return False

        new_vertex = VertexForAlgorithms(vertex)
        self.vertices[vertex] = new_vertex
        self.vertex_number += 1

        return True

    def construct_way(self, start, end):
        if self[end].source is None: return None, INF

        stack = Stack()
        current = end

        while True:
            stack.push(current)
            if current == start: break
            current = self[current].source()
            if current is None: return None

        way = []
        while not stack.empty():
            way.append(stack.pop())

        return way, self[end].distance()
