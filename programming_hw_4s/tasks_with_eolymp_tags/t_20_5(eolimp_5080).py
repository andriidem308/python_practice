class Graph:
    def __init__(self, adjacency_matrix):
        self.matrix = adjacency_matrix

    def amount(self):
        amt = 0
        vertices_num = len(self.matrix)

        for i in range(vertices_num):
            checker = 0

            for j in range(vertices_num):
                if self.matrix[i][j] == 1:
                    checker += 1

            if checker == 1: amt += 1

        return amt


if __name__ == "__main__":
    with open("input.txt") as file_in:
        with open("output.txt", "w") as file_out:
            n = int(file_in.readline())
            matrix = []

            for _ in range(n):
                matrix.append(list(map(int, file_in.readline().split())))

            graph = Graph(matrix)

            print(graph.amount(), file=file_out)
