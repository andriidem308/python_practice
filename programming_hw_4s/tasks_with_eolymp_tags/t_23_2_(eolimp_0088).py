class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.back = None

    def empty(self):
        return self.front is None and self.back is None

    def enqueue(self, item):
        new_node = Node(item)

        if self.empty():
            self.front = new_node
        else:
            self.back.next = new_node

        self.back = new_node

    def dequeue(self):
        if self.empty():
            raise Exception("Queue: 'dequeue' applied to empty container")

        current_front = self.front
        item = current_front.item
        self.front = self.front.next
        del current_front

        if self.front is None: self.back = None

        return item


class Labyrinth:
    directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

    def __init__(self, matrix, wall, cell):
        self.matrix = matrix
        self.wall = wall
        self.cell = cell

    def get_area(self, i, j):
        visited = [[0 for __ in range(len(self.matrix))]
                   for _ in range(len(self.matrix))]
        visited[i][j] = 1
        count = 0
        q = Queue()
        q.enqueue((i, j))
        while not q.empty():
            i, j = q.dequeue()
            count += 1

            for di, dj in Labyrinth.directions:
                ii, jj = i + di, j + dj
                if self.matrix[ii][jj] == self.cell and not visited[ii][jj]:
                    q.enqueue((ii, jj))
                    visited[ii][jj] = 1

        return count


def wave_second(labyrinth, start):
    n, m = len(labyrinth), len(labyrinth[0])
    wave_matrix = [[100000] * m for i in range(n)]

    q = Queue()
    q.enqueue(start)
    wave_matrix[start[0]][start[1]] = 0

    while not q.empty():
        current = q.dequeue()
        i, j = current[0], current[1]

        for k in range(len(dj)):
            i1, j1 = i + di[k], j + dj[k]
            if wave_matrix[i1][j1] == 100000 and labyrinth[i1][j1] != 'R' and labyrinth[i1][j1] != 'e':
                q.enqueue((i1, j1))
                wave_matrix[i1][j1] = wave_matrix[i][j] + 1

    return wave_matrix


def wave_first(labyrinth, second_wave, start):
    n = len(labyrinth)
    m = len(labyrinth[0])
    wave_matrix = [[100000] * m for i in range(n)]

    q = Queue()
    q.enqueue(start)
    wave_matrix[start[0]][start[1]] = 0

    while not q.empty():
        current = q.dequeue()
        i, j = current[0], current[1]
        for k in range(len(dj)):
            i1, j1 = i + di[k], j + dj[k]
            if wave_matrix[i1][j1] == 100000 and labyrinth[i1][j1] != 'R' and wave_matrix[i][j] + 1 < second_wave[i1][j1]:
                q.enqueue((i1, j1))
                wave_matrix[i1][j1] = wave_matrix[i][j] + 1

    return wave_matrix


if __name__ == "__main__":
    with open("input.txt") as file_in:
        with open("output.txt", "w") as file_out:
            di = [0, -1, 0, 1]
            dj = [-1, 0, 1, 0]
            start_1 = 0
            start_2 = 0
            end = 0

            tests = int(file_in.readline())

            for test in range(tests):
                n, m = map(int, file_in.readline().split())
                mtr = []

                for i in range(n):
                    mtr.append(list(file_in.readline()))
                    if 'g' in mtr[i]:
                        start_1 = (i, mtr[i].index('g'))
                    if 'l' in mtr[i]:
                        start_2 = (i, mtr[i].index('l'))
                    if 'e' in mtr[i]:
                        end = (i, mtr[i].index('e'))

                s_wave = wave_second(mtr, start_2)
                f_wave = wave_first(mtr, s_wave, start_1)

                print('YES' if f_wave[end[0]][end[1]] <= 1000 else 'NO', file=file_out)
