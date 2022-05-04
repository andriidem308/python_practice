from GraphForAlgorithms import GraphForAlgorithms
from VertexForAlgorithm import INF


def BelmanFord(graph: GraphForAlgorithms, start, end):
    for vertex in graph:
        vertex.set_distance(INF)
        vertex.set_source(None)

    for i in range(len(graph) - 1):
        for vertex in graph:
            for neighbour_key in vertex.neighbours:
                neighbour = graph[neighbour_key]

                new_dist = vertex.distance + vertex.weight(neighbour_key)

                if new_dist < neighbour.distance:
                    neighbour.set_distance(new_dist)
                    neighbour.set_source(vertex.key())

    return graph.construct_way(start, end)
