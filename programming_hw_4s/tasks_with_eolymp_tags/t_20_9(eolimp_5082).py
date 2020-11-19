class Graph:
    def __init__(self, matrix, vertices_num):
        self.matrix = matrix
        self.vertices_num = vertices_num

    def amount(self):
        degrees_array = []

        for i in range(self.vertices_num):
            degree = 0

            for j in range(self.vertices_num):
                if self.matrix[i][j] != 0:
                    degree += (1 if i != j else 2)

            degrees_array.append(degree)

        return degrees_array


if __name__ == "__main__":
    with open("input.txt") as file_in:
        with open("output.txt", "w") as file_out:
            n = int(file_in.readline())
            adjacency_matrix = []

            for _ in range(n):
                adjacency_matrix.append(list(map(int, file_in.readline().split())))

            graph = Graph(adjacency_matrix, n)
            d_arr = graph.amount()

            for d in range(n):
                print(d_arr[d], end=" ", file=file_out)
