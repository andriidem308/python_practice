def Dijkstra(graph, start, end):
    for vertex in graph:
        vertex.setDistance(INF)
        vertex.setSource(None)

        graph[start].setDistance(0)
        pq = PriorityQueue()             # Створюємо пріоритетну чергу
        pq.insert(start, 0)              # Додаємо у чергу початкову вершину з нульовим пріоритетом
        while not pq.empty():
            vertex_key = pq.extractMinimum()  # Беремо індекс вершини з черги з найнижчим пріоритетом
            vertex = graph[vertex_key]        # Беремо вершину за індексом
            for neighbor_key in vertex.neighbors():  # Для всіх сусідів поточної вершини
                neighbour = graph[neighbor_key]     # Беремо вершину-сусіда за ключем

                newDist = vertex.distance() + vertex.weight(neighbor_key)

                if newDist < neighbour.distance():
                    neighbour.setDistance(newDist)
                    neighbour.setSource(vertex_key)

                    if neighbor_key in pq:
                        pq.decreasePriority(neighbor_key, newDist)  # перераховуємо пріоритет в черзі
                    else: # або додаємо елемент до черги, якщо його там ще немає.
                        pq.insert(neighbor_key, newDist)

    return graph.constructWay(start, end)  # Повертаємо шлях та його вагу