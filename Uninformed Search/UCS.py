def ucs(graph, start, goal):
    visited = set()
    queue = [(0, start)]  # (cost, node)

    while queue:
        # Sort the queue by cost (ascending)
        queue.sort(key=lambda x: x[0])
        cost, vertex = queue.pop(0)  # Remove the lowest-cost node

        if vertex in visited:
            continue

        print(f"Visiting {vertex} with cumulative cost {cost}")
        visited.add(vertex)

        if vertex == goal:
            print(f"Goal '{goal}' found with cost {cost}")
            return

        for neighbor, edge_cost in graph.get(vertex, []):
            if neighbor not in visited:
                queue.append((cost + edge_cost, neighbor))

# Example graph with costs
graph = {
    'A': [('B', 1), ('C', 5)],
    'B': [('A', 1), ('D', 3), ('E', 1)],
    'C': [('A', 5), ('F', 2)],
    'D': [('B', 3)],
    'E': [('B', 1), ('F', 1)],
    'F': [('C', 2), ('E', 1)]
}

ucs(graph, 'A', 'F')  # Search from A to F
