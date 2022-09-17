from ..dijkstra import Dijkstra


graph = {'A': {'B': 25, 'C': 20, 'D': 10,"E":105},
         'B': {'A': 20, 'C': 15, 'D': 80,"E":80},
         'C': {'A': 30, 'B': 15,"D":70,"E":90},
         'D': {'A': 10, 'B': 10, 'C': 50, 'E': 100},
         'E': {'A': 40,"B": 50,"C": 5,"D": 10}}

def shortest_path(g:dict,start_node,end_node):

        dijkstra = Dijkstra(g, start_vertex=start_node)

         # Run the algorithm
        dijkstra.dijkstra()

         
        price = dijkstra.vertex_labels[end_node]["distance"]
        path = ""
        for vertex in dijkstra.vertices:
             if vertex == end_node:
                 path = dijkstra.build_path(vertex)
             else:
                 pass

        return price,path

print(shortest_path(graph,"A","D"))

# Output:
#         price     path
#        ( 10  , ['A', 'D'])

print(shortest_path(graph,"A","E"))
# Output:
#         price       path
#        ( 100 , ['A', 'D', 'B', 'E'])
