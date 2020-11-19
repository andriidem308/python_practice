class Graph:
    def __init__(self, vertex_num):
        self.vertices = {}
        for i in range(1, vertex_num + 1):
            self.vertices[i] = set()

    def add_edge(self, source, destination):
        self.vertices[source].add(destination)
        self.vertices[destination].add(source)

    def is_connected(self):
        remaining = set(self.vertices.keys())
        stack = [remaining.pop()]

        while stack:
            current = stack.pop()
            for neighbour in self.vertices[current]:
                if neighbour in remaining:
                    stack.append(neighbour)
                    remaining.remove(neighbour)

        return not remaining


if __name__ == '__main__':
    with open('input.txt') as file_in:
        with open('output.txt', 'w') as file_out:
            n, m = map(int, file_in.readline().split())
            graph = Graph(n)
            for _ in range(m):
                graph.add_edge(*map(int, file_in.readline().split()))
            print('YES' if graph.is_connected() else 'NO', file=file_out)