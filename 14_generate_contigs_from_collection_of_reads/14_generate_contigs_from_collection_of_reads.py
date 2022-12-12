from collections import defaultdict

with open("14_input.txt") as inp_fp:
    patterns = []
    while pattern := inp_fp.readline():
        patterns.append(pattern.strip())

graph = defaultdict(list)
for pattern in patterns:
    prefix = pattern[:-1]
    suffix = pattern[1:]
    graph[prefix].append(suffix)

in_vertices = defaultdict(lambda: 0)
out_vertices = defaultdict(lambda: 0)

for prefix in graph:
    out_vertices[prefix] = len(graph[prefix])
    for suffix in graph[prefix]:
        in_vertices[suffix] += 1
        # Otherwise program fails due to changing of dict size in the later for cycle
        # I spent inadequate time debugging it tbh
        out_vertices[suffix]

outpaths = []
for node in out_vertices:
    if not (in_vertices[node] == 1 and out_vertices[node] == 1):
        temp_path = []
        for next_node in graph[node]:
            new_path = [node, next_node]
            while in_vertices[next_node] == 1 and out_vertices[next_node] == 1:
                next_node = graph[next_node][0]
                new_path.append(next_node)
            temp_path.append(new_path)
        outpaths.extend(temp_path)

contigs = []
for path in outpaths:
    for kmer in path[1:]:
        path[0] += kmer[-1]
    contigs.append(path[0])

answer = " ".join(contigs)

with open("14_output.txt", "w+") as out_fp:
    out_fp.write(answer)
