from collections import defaultdict

with open("13_input.txt", "r") as inp_fp:
    k, d = [int(inp) for inp in inp_fp.readline().strip().split()]
    paired_reads = []
    while inp := inp_fp.readline().strip():
        paired_reads.append([element for element in inp.split("|") if element])

print(paired_reads)

suffixes = [(pair[0][1:], pair[1][1:]) for pair in paired_reads]
prefixes = [(pair[0][:-1], pair[1][:-1]) for pair in paired_reads]

graph = defaultdict(list)
for prefix, suffix in zip(prefixes, suffixes):
    graph[prefix].append(suffix)


def find_start_node():
    in_vertices = defaultdict(lambda: 0)
    for pre in prefixes:
        in_vertices[pre] = 0
    for suf in suffixes:
        in_vertices[suf] += 1

    min = len(graph) + 1
    min_vertice = None
    for vertice, value in in_vertices.items():
        if value < min:
            min_vertice = vertice
            min = value
        elif min == 0 and value == 0:
            raise Exception("No path")

    return min_vertice


# Modified algo from task 11
def find_eulerian_path():
    print(graph)
    start_node = find_start_node()
    unmarked_vertices = {i: lst.copy() for i, lst in graph.items()}
    q = []
    path = []
    q.append(start_node)
    while q:
        if unmarked_vertices.get(q[-1]):
            vertice = unmarked_vertices[q[-1]].pop()
            q.append(vertice)
        else:
            path.append(q[-1])
            q.pop()
    if len(path) >= len(graph):
        return reversed(path)
    raise Exception("No path")


path = list(find_eulerian_path())

answer = path[0][0]
answer += ''.join([pair[0][-1] for pair in path[1:d+2]])
answer += path[0][1]
answer += ''.join([pair[1][-1] for pair in path[1:]])

with open("13_output.txt", "w+") as out_fp:
    out_fp.write(answer)
