from ..dijkstra import Dijkstra
import pprint

graph = {'A': {'B': 25, 'C': 20, 'D': 10,"E":105},
         'B': {'A': 20, 'C': 15, 'D': 80,"E":80},
         'C': {'A': 30, 'B': 15,"D":70,"E":90},
         'D': {'A': 10, 'B': 10, 'C': 50, 'E': 100},
         'E': {'A': 40,"B": 50,"C": 5,"D": 10}}

dijkstra = Dijkstra(graph, start_vertex='A')

# Run the algorithm
dijkstra.dijkstra()

pprint.pprint(dijkstra.vertex_labels["E"]["distance"])

for vertex in dijkstra.vertices:
    dijkstra.build_path(vertex)
