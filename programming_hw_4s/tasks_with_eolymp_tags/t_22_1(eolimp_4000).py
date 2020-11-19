class Graph:
    def __init__(self, matrix):
        self.matrix = matrix

    def get_vertices_count(self, vertex):
        visited = {vertex - 1}
        stack = [vertex - 1]
        count = 0

        while stack:
            current = stack.pop()
            count += 1

            for neighbour, edge in enumerate(self.matrix[current]):
                if edge:
                    if neighbour not in visited:
                        stack.append(neighbour)
                        visited.add(neighbour)

        return count


if __name__ == '__main__':
    with open('input.txt') as file_in:
        with open('output.txt', 'w') as file_out:
            n, s = map(int, file_in.readline().split())
            adjacency_matrix = []

            for _ in range(n):
                adjacency_matrix.append(list(map(int, file_in.readline().split())))

            graph = Graph(adjacency_matrix)

            print(graph.get_vertices_count(s), file=file_out)