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

        if self.empty(): self.front = new_node
        else: self.back.next = new_node

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


def wave(labyrinth):
    n, m = len(labyrinth), len(labyrinth[0])
    wave_matrix = [[-1] * m for i in range(n)]
    count = 1

    for i in range(n):
        for j in range(m):
            if wave_matrix[i][j] == -1 and labyrinth[i][j] == '#':
                q = Queue()
                q.enqueue((i, j))
                wave_matrix[i][j] = count

                while not q.empty():
                    current = q.dequeue()
                    ii, jj = current[0], current[1]

                    for k in range(len(dj)):
                        i1, j1 = ii + di[k], jj + dj[k]
                        if is_goable(i1, j1, n, m) and wave_matrix[i1][j1] == -1 and labyrinth[i1][j1] == '#':
                            q.enqueue((i1, j1))
                            wave_matrix[i1][j1] = count

                count += 1

    return count


if __name__ == "__main__":
    with open("input.txt") as file_in:
        with open("output.txt", "w") as file_out:
            di = [0, -1, 0, 1]
            dj = [-1, 0, 1, 0]

            n, m = map(int, file_in.readline().split())
            matrix = []
            for i in range(n): matrix.append(list(file_in.readline()))

            print(wave(matrix) - 1, file=file_out)
