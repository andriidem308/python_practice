class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, key, neighbours):
        self.vertices[key] = neighbours

    def get_adjacency_matrix(self):
        matrix = []

        for i in range(1, len(self.vertices) + 1):
            matrix.append([])

            for j in range(1, len(self.vertices) + 1):
                matrix[i - 1].append(1 if (j in self.vertices[i]) else 0)

        return matrix


if __name__ == '__main__':
    with open('input.txt') as file_in:
        with open("output.txt", "w") as file_out:
            graph = Graph()
            n = int(file_in.readline())

            for i in range(1, n + 1):
                edges = tuple(map(int, file_in.readline().split()))[1:]
                graph.add_vertex(i, set(edges))

            for row in graph.get_adjacency_matrix():
                print(*row, file=file_out)
