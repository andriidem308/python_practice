class Graph:
    def __init__(self, vertices_num):
        self.vertices = {}
        for i in range(1, vertices_num + 1): self.vertices[i] = set()

    def add_edge(self, x, y):
        self.vertices[x].add(y)
        self.vertices[y].add(x)

    def shortest_path(self, start_node, final_node):

        paths_lengths = {start_node: 0}
        queue = [start_node]
        path = []

        while queue:
            current_node = queue.pop(0)
            path.append(current_node)
            for other in self.vertices[current_node]:
                if other not in paths_lengths:
                    paths_lengths[other] = paths_lengths[current_node] + 1

                    if other == final_node:
                        path.append(final_node)
                        return paths_lengths[other], path

                    queue.append(other)


if __name__ == "__main__":
    with open("input.txt") as file_in:
        with open("output.txt", "w") as file_out:
            n, m = list(map(int, file_in.readline().split()))
            a, b = list(map(int, file_in.readline().split()))

            graph = Graph(n)

            for _ in range(m):
                graph.add_edge(*map(int, file_in.readline().split()))

            try:
                min_length, st_path = graph.shortest_path(a, b)
                print(min_length, file=file_out)
                print(*st_path, file=file_out)
            except:
                print(-1, file=file_out)
