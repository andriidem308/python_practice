class Graph:
    def __init__(self, matrix):
        self.matrix = matrix

    def shortest_path(self, start_node, final_node):
        paths_lengths = {start_node-1: 0}
        queue = [start_node-1]

        while queue:
            current_node = queue.pop(0)

            for other, have_edge in enumerate(self.matrix[current_node]):
                if other not in paths_lengths and have_edge == 1:
                    paths_lengths[other] = paths_lengths[current_node] + 1

                    if other == final_node-1: return paths_lengths[other]

                    queue.append(other)

        return 0


if __name__ == "__main__":
    with open("input.txt") as file_in:
        with open("output.txt", "w") as file_out:
            n, s, f = list(map(int, file_in.readline().split()))
            adjacency_matrix = []

            for _ in range(n):
                adjacency_matrix.append(list(map(int, file_in.readline().split())))

            graph = Graph(adjacency_matrix)

            print(graph.shortest_path(s, f), file=file_out)

