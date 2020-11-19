class Graph:
    def __init__(self, adjacency_matrix):
        self.matrix = adjacency_matrix

    def get_components_count(self):
        remaining = set(range(len(self.matrix)))
        stack = []
        count = 0

        while remaining:
            if stack:
                current = stack.pop()
            else:
                current = remaining.pop()
                count += 1

            for neighbour, edge in enumerate(self.matrix[current]):
                if edge:
                    if neighbour in remaining:
                        stack.append(neighbour)
                        remaining.remove(neighbour)
        return count


if __name__ == '__main__':
    with open('input.txt') as file_in:
        with open('output.txt', 'w') as file_out:
            n = int(file_in.readline())
            matrix = []

            for _ in range(n):
                matrix.append(list(map(int, file_in.readline().split())))
            graph = Graph(matrix)

            print(graph.get_components_count(), file=file_out)