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


def is_goable(i, j, n):
    if i < 0 or i >= n or j < 0 or j >= n: return False
    return True


def wave(labyrinth, start):
    n = len(labyrinth)
    wave_matrix = [[-1] * n for i in range(n)]
    q = Queue()
    q.enqueue(start)
    wave_matrix[start[0]][start[1]] = 0

    while not q.empty():
        current = q.dequeue()
        i, j = current[0], current[1]

        for k in range(len(dj)):
            i1, j1 = i + di[k], j + dj[k]
            if is_goable(i1, j1, n) and wave_matrix[i1][j1] == -1 and labyrinth[i1][j1] != 'O':
                q.enqueue((i1, j1))
                wave_matrix[i1][j1] = wave_matrix[i][j] + 1

    return wave_matrix


def find_way(labyrinth, start, end):
    wave_matrix = wave(labyrinth, start)

    if wave_matrix[end[0]][end[1]] == -1:
        print('N')
        return

    n = len(wave_matrix)
    matrix = labyrinth

    matrix[end[0]][end[1]] = "+"

    current = end
    while True:
        if current == start:
            matrix[current[0]][current[1]] = "@"
            break

        i = current[0]
        j = current[1]

        for k in range(len(dj)):
            i1 = i + di[k]
            j1 = j + dj[k]

            current = None

            if is_goable(i1, j1, n) and wave_matrix[i1][j1] == wave_matrix[i][j] - 1:
                current = (i1, j1)
                matrix[i1][j1] = "+"
                break

    print('Y', file=file_out)
    for i in range(len(matrix)): print(''.join(matrix[i]), file=file_out)


if __name__ == "__main__":
    with open("input.txt") as file_in:
        with open("output.txt", "w") as file_out:
            di = [0, -1, 0, 1]
            dj = [-1, 0, 1, 0]

            start = 0
            end = 0

            n = int(file_in.readline())
            mtr = []

            for i in range(n):
                mtr.append(list(file_in.readline()))

                if '@' in mtr[i]: start = (i, mtr[i].index('@'))
                if 'X' in mtr[i]: end = (i, mtr[i].index('X'))

            find_way(mtr, start, end)
