from get_input import get_input
import igraph as ig
from functools import reduce

def parse_line(line: str) -> tuple[str, str]:
    first, second = line.strip().split("-")
    return first, second

connections = get_input(day=23)
def reduce_line(vertices: set[str], line: str) -> set[str]:
    first, second = parse_line(line)
    vertices.add(first)
    vertices.add(second)
    return vertices

unique_vertices = reduce(reduce_line, connections, set())
vertex_to_index: dict[str, int] = dict()
index_to_vertex: dict[int, str] = dict()

for i, vertex in enumerate(unique_vertices):
    vertex_to_index[vertex] = i
    index_to_vertex[i] = vertex

edges = []
for line in connections:
    first, second = parse_line(line)
    edges.append((vertex_to_index[first], vertex_to_index[second]))
graph = ig.Graph(edges=edges, directed=False)

lan_parties: set[set[str]] = set()
for vertex in graph.vs:
    for vertex_2 in vertex.neighbors():
        for vertex_3 in vertex_2.neighbors():
            lan_party_names = [index_to_vertex[v.index] for v in [vertex, vertex_2, vertex_3]]
            has_t_name = any([v.startswith("t") for v in lan_party_names])
            print(lan_party_names, has_t_name)
            if has_t_name and vertex in vertex_3.neighbors():
                lan_parties.add(frozenset([vertex.index, vertex_2.index, vertex_3.index]))

print(len(lan_parties))

names = [index_to_vertex[index] for index in list(graph.largest_cliques()[0])]
print(",".join(sorted(names)))