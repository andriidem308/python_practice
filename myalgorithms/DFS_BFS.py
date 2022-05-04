from Graph import Graph
from Queue import Queue


def DFS(graph, start):
    visited = set()
    __dfs_helper(graph, visited, start)
    return visited


def __dfs_helper(graph, visited, start):
    print(start, end=" ")
    visited.add(start)

    for neighbour in graph[start].neighbours:
        if neighbour not in visited:
            __dfs_helper(graph, visited, neighbour)


def BFS(graph, start):
    visited = set()
    q = Queue()
    q.enqueue(start)
    visited.add(start)
    while not q.empty():
        current = q.enqueue()
        print(current)
        for neighbour in graph[current].neighbours():
            if neighbour not in visited:
                q.enqueue(neighbour)
                visited.add(neighbour)

    return visited


g = Graph(True)

g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(2, 5)
g.add_edge(3, 5)
g.add_edge(3, 6)
g.add_edge(4, 3)
g.add_edge(4, 6)
g.add_edge(5, 4)
g.add_edge(5, 6)

print("---- DFS ----")
DFS(g, 1)
print()
DFS(g, 5)
print()
DFS(g, 4)
print()
DFS(g, 2)
print()
print("---- BFS ----")
DFS(g, 4)
print()
DFS(g, 2)
print()

