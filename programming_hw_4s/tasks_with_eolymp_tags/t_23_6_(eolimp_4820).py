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


def is_goable(i, j, n, m):
    if i < 0 or i >= n or j < 0 or j >= m: return False
    return True


def wave(labyrinth, start, end):
    n, m = len(labyrinth), len(labyrinth[0])
    wave_matrix = [[-1] * m for i in range(n)]

    q = Queue()
    q.enqueue(start)
    wave_matrix[start[0]][start[1]] = 0

    while not q.empty():
        current = q.dequeue()
        i, j = current[0], current[1]

        for k in range(len(dj)):
            i1, j1 = i + di[k], j + dj[k]
            if is_goable(i1, j1, n, m) and wave_matrix[i1][j1] == -1 and labyrinth[i1][j1] == 0:
                q.enqueue((i1, j1))
                wave_matrix[i1][j1] = wave_matrix[i][j] + 1
                if end[0] == i1 and end[1] == j1: break

    return wave_matrix[end[0]][end[1]] if wave_matrix[end[0]][end[1]] != -1 else -1


if __name__ == "__main__":
    with open("input.txt") as file_in:
        with open("output.txt", "w") as file_out:
            di = [0, -1, 0, 1]
            dj = [-1, 0, 1, 0]
            start = 0
            end = 0

            n, m = map(int, file_in.readline().split())
            matrix = []
            for i in range(n): matrix.append(list(map(int, file_in.readline().split())))
            start = list(map(int, file_in.readline().split()))
            end = list(map(int, file_in.readline().split()))

            start[0], start[1] = start[1] - 1, start[0] - 1
            end[0], end[1] = end[1] - 1, end[0] - 1

            print(wave(matrix, start, end), file=file_out)
