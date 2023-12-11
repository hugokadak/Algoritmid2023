import heapq

def dijkstra(graph, start, end):
    # Initialize distances with infinity for all nodes except the start node
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    # Use a priority queue to keep track of nodes with their current distances
    priority_queue = [(0, start)]
    
    # Store predecessors to reconstruct the path
    predecessors = {node: None for node in graph}
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # If current distance is greater than the stored distance, skip
        if current_distance > distances[current_node]:
            continue
        
        # Stop the algorithm when the end node is reached
        if current_node == end:
            break
        
        # Update distances and predecessors for neighboring nodes
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    
    # Reconstruct the path
    path = []
    current = end
    while current is not None:
        path.insert(0, current)
        current = predecessors[current]
    
    return distances[end], path  # Return the shortest distance and the path

# Example usage:
# Define a graph as an adjacency list
graph = {
        'Kuressaare':{'Pärnu': 154, 'Haapsalu': 157},
        'Haapsalu':{'Kuressaare': 157, 'Keila': 76, 'Rapla': 90},
        'Keila':{'Haapsalu': 76, 'Tallinn': 28},
        'Tallinn':{'Keila': 28, 'Pärnu': 127, 'Viljandi': 153, 'Rapla': 54, 'Tartu': 181,'Rakvere':100},
        'Rapla':{'Tallinn': 54, 'Haapsalu': 90, 'Paide': 59},
        'Pärnu':{'Tallinn': 127, 'Kuressaare': 154, 'Valga': 140, 'Viljandi': 92},
        'Valga':{'Pärnu': 140, 'Viljandi': 80, 'Tartu': 85, 'Otepää': 48, 'Võru': 70},
        'Viljandi':{'Valga': 80, 'Pärnu': 92, 'Tallinn': 153, 'Paide': 70, 'Tartu': 78},
        'Paide':{'Rapla': 59, 'Viljandi': 70, 'Tapa': 55, 'Tartu': 103},
        'Tapa':{'Paide': 55, 'Rakvere': 31,'Tartu': 126},
        'Rakvere':{'Jõhvi': 72, 'Tapa': 31, 'Tallinn': 100},
        'Jõhvi':{'Rakvere': 72, 'Tartu': 129, 'Narva': 50},
        'Narva':{'Jõhvi': 50},
        'Tartu':{'Jõhvi': 129, 'Viljandi': 78, 'Tallinn': 181, 'Tapa': 126, 'Valga': 85, 'Paide': 103, 'Otepää': 43, 'Võru': 71},
        'Otepää':{'Võru': 43, 'Tartu': 43, 'Valga': 48},
        'Võru':{'Tartu': 71, 'Valga': 70, 'Otepää': 43},
}

# Start and end nodes for Dijkstra's algorithm
start_node = 'Narva'
end_node = 'Viljandi'

# Run Dijkstra's algorithm
shortest_distance, path = dijkstra(graph, start_node, end_node)

# Print the result
print("Shortest distance from node {} to node {}: {}".format(start_node, end_node, shortest_distance))
print("Shortest path:", ' -> '.join(path))