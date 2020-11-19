class Graph:
    def __init__(self, vertices_num):
        self.vertices = {}
        for i in range(1, vertices_num + 1): self.vertices[i] = set()

    def add_edge(self, begin, end):
        self.vertices[begin].add(end)
        self.vertices[end].add(begin)

    def dfs(self, visited: list, burning: set, steps=0):
        if len(visited) == len(self.vertices):
            return burning, steps

        tmp = set()
        for bv in burning:
            for v in self.vertices[bv]:
                if v not in visited:
                    visited.append(v)
                    tmp.add(v)

        return self.dfs(visited, tmp, steps+1)


if __name__ == "__main__":
    with open("input.txt") as file_in:
        with open("output.txt", "w") as file_out:
            n, m = list(map(int, file_in.readline().split()))

            graph = Graph(n)

            for _ in range(m):
                vertex_x, vertex_y = list(map(int, file_in.readline().split()))
                graph.add_edge(vertex_x, vertex_y)

            k = int(file_in.readline())
            burned_arr = set(map(int, file_in.readline().split()))

            last_move, steps_amount = graph.dfs([bv for bv in burned_arr], burned_arr)
            print(steps_amount, min(last_move), sep="\n", file=file_out)