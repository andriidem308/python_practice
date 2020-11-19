class Graph:
    def __init__(self, edges_array, vertices_num):
        self.edges_array = edges_array
        self.vertices_num = vertices_num

    def amount(self):
        degrees_array = []

        for i in range(1, self.vertices_num + 1):
            in_degree = out_degree = 0

            for j in range(len(self.edges_array)):
                if self.edges_array[j][1] == i: in_degree += 1
                if self.edges_array[j][0] == i: out_degree += 1

            degrees_array.append([in_degree, out_degree])

        return degrees_array


if __name__ == "__main__":
    with open("input.txt") as file_in:
        with open("output.txt", "w") as file_out:
            n, m = (map(int, file_in.readline().split()))
            matrix = []

            for _ in range(m):
                matrix.append(list(map(int, file_in.readline().split())))

            graph = Graph(matrix, n)
            d_arr = graph.amount()

            for io in range(len(d_arr)):
                print(*d_arr[io], file=file_out)
