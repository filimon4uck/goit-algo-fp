import heapq
import matplotlib.pyplot as plt
import networkx as nx

def dijkstra_with_heap(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    paths = {node: [] for node in graph}
    paths[start] = [start]
    
 
    heap = [(0, start)]
    
    while heap:
        current_distance, current_node = heapq.heappop(heap)
        
        
        if current_distance > distances[current_node]:
            continue
        
       
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                paths[neighbor] = paths[current_node] + [neighbor]
                heapq.heappush(heap, (distance, neighbor))
    
    return distances, paths



graph = {
    'A': [('B', 5), ('C', 10)],
    'B': [('A', 5), ('D', 3)],
    'C': [('A', 10), ('D', 2)],
    'D': [('B', 3), ('C', 2), ('E', 4)],
    'E': [('D', 4)]
}


start_node = 'A'
distances, paths = dijkstra_with_heap(graph, start_node)
print("Найкоротші відстані від вершини", start_node)
for node, distance in distances.items():
    print(f"Вершина {node}: відстань = {distance}, шлях = {paths[node]}")

G = nx.Graph()

for node, neighbors in graph.items():
    for neighbor, weight in neighbors:
        G.add_edge(node, neighbor, weight=weight)

pos = nx.spring_layout(G, seed=42)

shortest_edges = []
for target_node, path in paths.items():
    edges_in_path = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
    shortest_edges.extend(edges_in_path)

nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, width=2)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)


nx.draw_networkx_edges(
    G, pos,
    edgelist=shortest_edges,
    edge_color="red",
    width=3
)

plt.show()
