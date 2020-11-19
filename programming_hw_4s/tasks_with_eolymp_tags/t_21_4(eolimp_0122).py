class Graph:
    def __init__(self, vertices_num):
        self.vertices = {}
        for i in range(1, vertices_num + 1): self.vertices[i] = set()

    def add_edge(self, begin, end):
        self.vertices[begin].add(end)

    def find_paths(self, start_vertex, end_vertex, days, path=[], visited=[]):
        path = path + [start_vertex]

        if days < 0: return []
        if start_vertex == end_vertex: return [path]

        paths = []

        for vertex in self.vertices[start_vertex]:
            if vertex not in visited:
                new_paths = self.find_paths(vertex, end_vertex, days-1, path, visited+[start_vertex])
                for new_path in new_paths: paths.append(new_path)

        return paths


if __name__ == "__main__":
    with open("input.txt") as file_in:
        with open("output.txt", "w") as file_out:
            n, k, a, b, d = list(map(int, file_in.readline().split()))
            graph = Graph(n)

            for _ in range(k):
                vertex_x, vertex_y = list(map(int, file_in.readline().split()))
                graph.add_edge(vertex_x, vertex_y)

            print(len(graph.find_paths(a, b, d)), file=file_out)
            

