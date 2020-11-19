LIMIT = 10**3


class DirectedGraph:
    def __init__(self, edges):
        self.edges = [new_edge(*edge) for edge in edges]

    def add_edge(self, fst, snd, weight=1, d_linked=True):
        self.edges.append(Edge(start=fst, end=snd, weight=weight))
        if d_linked: self.edges.append(Edge(start=snd, end=fst, weight=weight))

    def remove_edge(self, fst, snd, d_linked=True):
        pairs = self.get_pairs(fst, snd, d_linked)
        local_edges = self.edges.copy()

        for e in local_edges:
            if [e.start, e.end] in pairs: self.edges.remove(e)

    @property
    def vertices(self):
        return set(sum(([edge.start, edge.end] for edge in self.edges), []))

    @property
    def get_linked(self):
        linked_vertices = {vertex: set() for vertex in self.vertices}
        for current_edge in self.edges:
            linked_vertices[current_edge.start].add((current_edge.end, current_edge.weight))

        return linked_vertices

    @staticmethod
    def get_pairs(fst, snd, d_linked=True):
        if d_linked: t_pair = [[fst, snd], [snd, fst]]
        else: t_pair = [[fst, snd]]

        return t_pair

    def dijkstra_algorithm(self, first, second):
        weights = {vertex: LIMIT for vertex in self.vertices}
        chosen_vertices = {vertex: None for vertex in self.vertices}
        weights[first] = 0
        vertices = self.vertices.copy()

        while vertices:
            curr = min(vertices, key=lambda vertex: weights[vertex])
            vertices.remove(curr)
            if weights[curr] == LIMIT: break

            for other, weight in self.get_linked[curr]:
                new_weight = weights[curr] + weight

                if new_weight < weights[other]:
                    weights[other] = new_weight
                    chosen_vertices[other] = curr

        return weights[second]


def new_edge(a, b, weight=1): return Edge(a, b, weight)


if __name__ == "__main__":
    with open("input.txt") as file_in:
        with open("output.txt", "w") as file_out:
            from collections import namedtuple
            Edge = namedtuple('Edge', 'start, end, weight')
            n, f, s = list(map(int, file_in.readline().split()))
            new_edges = []

            for i in range(n):
                tmp_row = list(map(int, file_in.readline().split()))
                for j in range(n):
                    if tmp_row[j] not in (-1, 0):
                        new_edges.append((str(i + 1), str(j + 1), tmp_row[j]))

            graph = DirectedGraph(new_edges)

            print(graph.dijkstra_algorithm(str(f), str(s)), file=file_out)
