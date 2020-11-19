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
    if i < 0 or i >= n or j < 0 or j >= n:
        return False
    return True


def wave(maze, wave_matrix, start, count):
    n = len(maze)
    q = Queue()
    q.enqueue((start[0], start[1]))
    wave_matrix[start[0]][start[1]] = 1

    while not q.empty():
        current = q.dequeue()
        i, j = current[0], current[1]

        for k in range(len(dj)):
            i1, j1 = i + di[k], j + dj[k]

            if is_goable(i1, j1, n) and wave_matrix[i1][j1] == -1 and maze[i1][j1] == '.':
                q.enqueue((i1, j1))
                wave_matrix[i1][j1] = 1
            elif not is_goable(i1, j1, n) or maze[i1][j1] == '#':
                count[0] += 1

    return count


if __name__ == "__main__":
    with open("input.txt") as file_in:
        with open("output.txt", "w") as file_out:
            di = [0, -1, 0, 1]
            dj = [-1, 0, 1, 0]
            start = 0
            end = 0

            n = int(file_in.readline())
            matrix = []
            for i in range(n): matrix.append(list(file_in.readline()))

            count = [0]
            waveMatrix = [[-1] * n for i in range(n)]
            wave(matrix, waveMatrix, (0, 0), count)
            if waveMatrix[n - 1][n - 1] == -1: wave(matrix, waveMatrix, (n - 1, n - 1), count)

            print((count[0] - 4) * 9, file=file_out)
