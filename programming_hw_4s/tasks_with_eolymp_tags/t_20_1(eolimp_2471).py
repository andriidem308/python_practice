class Graph:
    def __init__(self, adjacency_matrix):
        self.matrix = adjacency_matrix

    def get_list_of_edges(self):
        vertices_lst = []
        vertices_num = len(self.matrix)

        for ii in range(vertices_num):
            neighbors = []

            for jj in range(ii + 1, vertices_num):
                if self.matrix[ii][jj] == 1:
                    neighbors.append(jj)

            vertices_lst.append(neighbors)

        return vertices_lst


if __name__ == '__main__':
    with open('input.txt') as file_in:
        with open("output.txt", "w") as file_out:
            n = int(file_in.readline())
            matrix = []

            for _ in range(n):
                matrix.append(list(map(int, file_in.readline().split())))

            graph = Graph(matrix)
            vertices = graph.get_list_of_edges()

            for i in range(n):
                for j in vertices[i]:
                    print(i + 1, j + 1, file=file_out)

