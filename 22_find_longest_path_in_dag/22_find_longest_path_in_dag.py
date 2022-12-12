from collections import defaultdict

with open("22_input.txt") as inp_fp:
    from_node = int(inp_fp.readline().strip())
    to_node = int(inp_fp.readline().strip())
    max_node = max(from_node, to_node)
    graph = defaultdict(lambda: [])
    while line := inp_fp.readline():
        temp_from_node = int(line.split("->")[0])
        temp_info = line.split("->")[1]
        temp_to_node = int(temp_info.split(":")[0])
        temp_node_weight = int(temp_info.split(":")[1])
        graph[temp_from_node].append([temp_to_node, temp_node_weight])
        max_node = max(max_node, max(temp_to_node, temp_from_node))

print(graph)


def find_dag_longest_path(source, goal):
    inf = 10 ** 9
    dist = [-inf for _ in range(max_node + 1)]
    path = defaultdict(int)
    visited = defaultdict(lambda: False)
    q = []
    dist[source] = 0

    for i in range(max_node + 1):
        if visited[i] is False:
            query = [i]
            while len(query) > 0:
                node = query[-1]
                visited[node] = True
                found_not_visited = False
                for node in graph[node]:
                    if visited[node[0]] is False:
                        query.append(node[0])
                        found_not_visited = True
                        break
                if not found_not_visited:
                    q.append(query.pop())

    while len(q) > 0:
        u = q.pop()
        if dist[u] != inf:
            for i in graph[u]:
                if dist[i[0]] < dist[u] + i[1]:
                    dist[i[0]] = dist[u] + i[1]
                    path[i[0]] = u

    final_path = [goal]
    current = goal
    while current != source:
        final_path.append(path[current])
        current = path[current]

    return dist[goal], list(reversed(final_path))


length, path = find_dag_longest_path(from_node, to_node)
formatted_path = "->".join([str(node) for node in path])
answer = "\n".join([str(length), formatted_path])
with open("22_output.txt", "w+") as out_fp:
    out_fp.write(answer)
