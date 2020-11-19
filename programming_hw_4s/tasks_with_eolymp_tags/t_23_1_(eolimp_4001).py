DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1))


class Labyrinth:
    def __init__(self, matrix, wall, cell):
        self.matrix = matrix
        self.wall = wall
        self.cell = cell

    def get_area(self, r, c):
        visited = [[0 for __ in range(len(matrix))] for _ in range(len(matrix))]
        visited[r][c] = 1
        count = 0

        queue = [(r, c)]

        while queue:
            r, c = queue.pop(0)
            count += 1

            for di, dj in DIRECTIONS:
                ii, jj = r + di, c + dj

                if self.matrix[ii][jj] == self.cell and not visited[ii][jj]:
                    queue.append((ii, jj))
                    visited[ii][jj] = 1

        return count


if __name__ == '__main__':
    with open('input.txt') as file_in:
        with open('output.txt', 'w') as file_out:
            matrix = []

            n = int(file_in.readline())
            for _ in range(n): matrix.append(list(file_in.readline()))
            row, column = map(int, file_in.readline().split())

            print(Labyrinth(matrix, '*', '.').get_area(row - 1, column - 1), file=file_out)