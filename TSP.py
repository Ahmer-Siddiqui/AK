from itertools import permutations

# Function to calculate the cost of a given path
def calculate_cost(graph, path):
    cost = 0
    n = len(path)
    for i in range(n - 1):
        cost += graph[path[i]][path[i + 1]]
    cost += graph[path[-1]][path[0]]  # return to start
    return cost

# Function to find the shortest path using brute force
def tsp_brute_force(graph):
    n = len(graph)
    cities = list(range(n))
    min_path = []
    min_cost = float('inf')

    for perm in permutations(cities[1:]):  # fix starting city as 0
        current_path = [0] + list(perm)
        current_cost = calculate_cost(graph, current_path)

        if current_cost < min_cost:
            min_cost = current_cost
            min_path = current_path

    return min_path + [0], min_cost  # return to starting point

# Sample graph as adjacency matrix
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Run the algorithm
path, cost = tsp_brute_force(graph)

# Display result
print("Minimum cost path:", ' -> '.join(map(str, path)))
print("Minimum cost:", cost)  