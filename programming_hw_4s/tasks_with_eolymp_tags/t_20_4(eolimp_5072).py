class Graph:
    def __init__(self, adjacency_matrix):
        self.matrix = adjacency_matrix

    def get_count_of_edges(self):
        cnt = 0
        vertices_num = len(self.matrix)

        for i in range(vertices_num):
            for j in range(vertices_num):
                if self.matrix[i][j] == 1:
                    cnt += 1
        return cnt


if __name__ == '__main__':
    with open('input.txt') as file_in:
        with open("output.txt", "w") as file_out:
            n = int(file_in.readline())
            matrix = []

            for _ in range(n):
                matrix.append(list(map(int, file_in.readline().split())))

            graph = Graph(matrix)
            print(graph.get_count_of_edges(), file=file_out)

            