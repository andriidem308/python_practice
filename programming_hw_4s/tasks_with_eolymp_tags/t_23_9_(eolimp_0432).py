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
        if self.empty(): raise Exception("Queue: 'dequeue' applied to empty container")

        current_front = self.front
        item = current_front.item
        self.front = self.front.next
        del current_front

        if self.front is None: self.back = None

        return item


def is_goable(i, j, k, n, m, l):
    if i < 0 or i >= n or j < 0 or j >= m or k < 0 or k >= l:
        return False
    return True


def wave(labyrinth, start, end):
    n, m, l = len(labyrinth), len(labyrinth[0]), len(labyrinth[0][0])
    wave_matrix = [[[-1] * l for __ in range(m)] for _ in range(n)]
    q = Queue()
    q.enqueue((start[0], start[1], start[2]))
    wave_matrix[start[0]][start[1]][start[2]] = 0

    while not q.empty():
        current = q.dequeue()
        i, j, k = current[0], current[1], current[2]

        for s in range(len(dj)):
            i1, j1, k1 = i + di[s], j + dj[s], k + dk[s]
            if is_goable(i1, j1, k1, n, m, l) and wave_matrix[i1][j1][k1] == -1 and labyrinth[i1][j1][k1] != '#':
                q.enqueue((i1, j1, k1))
                wave_matrix[i1][j1][k1] = wave_matrix[i][j][k] + 1

    return wave_matrix[end[0]][end[1]][end[2]]


if __name__ == "__main__":
    with open("input.txt") as file_in:
        with open("output.txt", "w") as file_out:
            di = [0, 0, -1, 0, 0, 1]
            dj = [0, -1, 0, 0, 1, 0]
            dk = [-1, 0, 0, 1, 0, 0]

            start = 0
            end = 0

            x1, x2, x3 = map(int, file_in.readline().split())
            while x1 + x2 + x3 != 0:
                matrix = []
                for i in range(x1):
                    matrix.append([])
                    for j in range(x2):
                        matrix[i].append(list(file_in.readline()))
                        if 'S' in matrix[i][j]: start = (i, j, matrix[i][j].index('S'))
                        if 'E' in matrix[i][j]: end = (i, j, matrix[i][j].index('E'))
                    file_in.readline()

                x = wave(matrix, start, end)
                print('Trapped!' if x == -1 else f'Escaped in {x} minute(s).', file=file_out)
                x1, x2, x3 = map(int, file_in.readline().split())
