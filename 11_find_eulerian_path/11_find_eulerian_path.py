from collections import defaultdict

graph = [[]]
edges_count = 0
with open("11_input.txt", "r") as inp_fp:
    while line := inp_fp.readline():
        from_node, to_nodes = line.split(" -> ")
        from_node = int(from_node)
        to_nodes = [int(node) for node in to_nodes.split(",")]
        edges_count += len(to_nodes)
        max_node = max(from_node, max(to_nodes))
        while len(graph) < max_node + 1:
            graph.append([])
        graph[from_node].extend(to_nodes)

# print(graph)


def make_edge(node_from, node_to):
    return f"{node_from}->{node_to}"


def find_start_end_nodes():
    in_out_vertices = defaultdict(lambda: [0, 0])
    for i, lst in enumerate(graph):
        in_out_vertices[i][1] = len(lst)

    for lst in graph:
        for v in lst:
            in_out_vertices[v][0] += 1

    start_node = None
    end_node = None
    for i, val in in_out_vertices.items():
        if val[0] == val[1] + 1:
            if end_node is not None:
                raise Exception("No path")
            end_node = i
        elif val[1] == val[0] + 1:
            if start_node is not None:
                raise Exception("No path")
            start_node = i
        elif val[0] != val[1]:
            raise Exception("No path")

    return start_node, end_node

# TOO SLOW, MAYBE BUGGED
# start_node, _ = find_start_end_nodes()
# print(find_start_end_nodes())
#
#
# def dfs():
#     temp = dfs_iter(start_node, [], set())
#     if temp:
#         return temp
#
#
# def dfs_iter(edge, path, edges):
#     ways = graph[edge]
#     path.append(edge)
#     # print(path)
#     if len(edges) == edges_count:
#         return path
#     for w in ways:
#         if not make_edge(edge, w) in edges:
#             edges.add(make_edge(edge, w))
#             possible_path = dfs_iter(w, path, edges)
#             if possible_path is not None:
#                 return possible_path
#             edges.remove(make_edge(edge, w))
#     path.pop()
#
#
# path = dfs()


def find_eulerian_path():
    unmarked_vertices = [set(lst) for lst in graph]
    q = []
    path = []
    start_node, end_node = find_start_end_nodes()
    print(start_node, end_node)
    met_edges = set()

    # Phantom edge for algo to work (odd edge is cut by unmarked vertices tracker)
    if start_node is not None:
        graph[start_node].append(end_node)
    q.append(start_node or 0)
    while q:
        if unmarked_vertices[q[-1]]:
            vertice = unmarked_vertices[q[-1]].pop()
            met_edges.add(make_edge(q[-1], vertice))
            q.append(vertice)
        else:
            path.append(str(q[-1]))
            q.pop()
    return reversed(path)


path = find_eulerian_path()

with open("11_output.txt", "w+") as out_fp:
    out_fp.write("->".join([str(p) for p in path]))
