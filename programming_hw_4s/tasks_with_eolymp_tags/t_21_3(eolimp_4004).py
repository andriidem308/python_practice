class Graph:
    def __init__(self, matrix):
        self.matrix = matrix

    def has_cycle(self):
        remaining = set(range(len(self.matrix)))

        path = set()

        sources = {}
        current_neighbours = []

        while remaining:
            if current_neighbours:
                current_vertex = current_neighbours.pop()
                remaining.remove(current_vertex)
            else:
                current_vertex = remaining.pop()
                path.clear()
                sources.clear()
                sources[current_vertex] = None

            path.add(current_vertex)
            flag = True

            for neighbour, edge in enumerate(self.matrix[current_vertex]):
                if edge == 1:
                    if neighbour in path: return True
                    elif neighbour in remaining and neighbour not in sources:
                        current_neighbours.append(neighbour)
                        sources[neighbour] = current_vertex
                        flag = False

            if flag and current_neighbours:
                while current_vertex != sources[current_neighbours[-1]]:
                    path.remove(current_vertex)
                    current_vertex = sources.pop(current_vertex)

        return False


if __name__ == "__main__":
    with open("input.txt") as file_in:
        with open("output.txt", "w") as file_out:
            n = int(file_in.readline())
            adjacency_matrix = []

            for _ in range(n):
                adjacency_matrix.append(list(map(int, file_in.readline().split())))

            graph = Graph(adjacency_matrix)

            print(1 if graph.has_cycle() else 0, file=file_out)


