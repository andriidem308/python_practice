class Edge:
    def __init__(self, a, b):
        self.x = a
        self.y = b


n, m = map(int, input().split())

graph = []
tree = []
variety = [0] * (n+1)

for i in range(1, n+1): variety[i] = i
for i in range(m):
    a, b = map(int, input().split())
    new_edge = Edge(a, b)
    graph.append(new_edge)

for i in range(1, m+1):
    a = graph[i-1].x
    b = graph[i-1].y

    if variety[a] != variety[b]:
        tree.append(graph[i-1])
        old_variety, new_variety = variety[b], variety[a]

        for j in range(n):
            if variety[j] == old_variety: variety[j] = new_variety


for i in range(n-1):
    print(tree[i].x, tree[i].y)