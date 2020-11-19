class Graph:
    def __init__(self, vertices_num):
        self.vertices = {}

        for i in range(1, vertices_num + 1):
            self.vertices[i] = []

    def add_edge(self, source, destination):
        self.vertices[source].append(destination)
        self.vertices[destination].append(source)

    def get_neighbours(self, vertex):
        return tuple(neighbour for neighbour in self.vertices[vertex])


if __name__ == '__main__':
    with open('input.txt') as file_in:
        with open("output.txt", "w") as file_out:
            n = int(file_in.readline())
            graph = Graph(n)
            k = int(file_in.readline())

            for _ in range(k):
                cmd = file_in.readline().split()
                if cmd[0] == '1': graph.add_edge(int(cmd[1]), int(cmd[2]))
                elif cmd[0] == '2': print(*graph.get_neighbours(int(cmd[1])), file=file_out)
