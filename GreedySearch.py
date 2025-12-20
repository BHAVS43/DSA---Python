def greedy_coloring(graph, V):
    # Result stores color of each vertex
    result = [-1] * V
    result[0] = 0
    for u in range(1, V):
        used_colors = set()

        for v in graph[u]:
            if result[v] != -1:
                used_colors.add(result[v])

        color = 0
        while color in used_colors:
            color += 1

        result[u] = color

    for i in range(V):
        print(f"Vertex {i} ---> Color {result[i]}")

if __name__ == "__main__":
    V = 5
    graph = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1, 3],
        3: [1, 2, 4],
        4: [3]
    }

    greedy_coloring(graph, V)
