"""
Dijkstra's Algorithm
Find shortest path in weighted graph (positive weights only).
"""

import heapq

def dijkstra(graph, start, end):
    """
    Find shortest path from start to end using Dijkstra's algorithm.
    
    Args:
        graph: dict {node: [(neighbor, weight), ...]}
        start: starting node
        end: ending node
    
    Returns:
        (distance, path)
    """
    # Initialize distances
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Track previous node for path reconstruction
    previous = {node: None for node in graph}
    
    # Min heap: (distance, node)
    heap = [(0, start)]
    visited = set()
    
    while heap:
        current_dist, current_node = heapq.heappop(heap)
        
        # Skip if already visited
        if current_node in visited:
            continue
        
        visited.add(current_node)
        
        # If reached end, we can break early
        if current_node == end:
            break
        
        # Update distances through current node
        for neighbor, weight in graph[current_node]:
            if neighbor not in visited:
                new_distance = current_dist + weight
                
                # Found shorter path
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = current_node
                    heapq.heappush(heap, (new_distance, neighbor))
    
    # Reconstruct path
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = previous[node]
    path.reverse()
    
    return distances[end], path

# Example 1: Basic usage
print("=== Dijkstra's Algorithm ===\n")

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('C', 2)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 2), ('C', 1)]
}

distance, path = dijkstra(graph, 'A', 'D')
print(f"Shortest path A→D:")
print(f"  Distance: {distance}")
print(f"  Path: {' → '.join(path)}")

# Example 2: Another path
distance, path = dijkstra(graph, 'A', 'C')
print(f"\nShortest path A→C:")
print(f"  Distance: {distance}")
print(f"  Path: {' → '.join(path)}")

# Example 3: Real-world - Flight routing
print("\n=== Real World: Flight Routes ===")

flights = {
    'NYC': [('LA', 5), ('MIA', 2), ('CHI', 3)],
    'LA': [('NYC', 5), ('SF', 1)],
    'MIA': [('NYC', 2)],
    'CHI': [('NYC', 3), ('ATL', 2)],
    'ATL': [('CHI', 2), ('MIA', 4)],
    'SF': [('LA', 1)]
}

distance, path = dijkstra(flights, 'NYC', 'SF')
print(f"Cheapest flight NYC→SF:")
print(f"  Cost: ${distance}00")
print(f"  Route: {' → '.join(path)}")

# Example 4: All shortest distances
def dijkstra_all(graph, start):
    """Return shortest distances to all nodes."""
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    heap = [(0, start)]
    visited = set()
    
    while heap:
        current_dist, current_node = heapq.heappop(heap)
        
        if current_node in visited:
            continue
        
        visited.add(current_node)
        
        for neighbor, weight in graph[current_node]:
            if neighbor not in visited:
                new_distance = current_dist + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(heap, (new_distance, neighbor))
    
    return distances

print("\n=== Distances from NYC ===")
distances = dijkstra_all(flights, 'NYC')
for city, dist in sorted(distances.items()):
    print(f"  NYC → {city}: ${dist}00")

print("\n=== Complexity Analysis ===")
print("Time:  O((V + E) log V) with min-heap")
print("       - Pop: V times")
print("       - Push: E times total")
print("       - Heap operations: O(log V)")
print("Space: O(V) for distances and heap")
