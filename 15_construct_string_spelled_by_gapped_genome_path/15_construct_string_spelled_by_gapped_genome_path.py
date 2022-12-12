from collections import defaultdict

with open("15_input.txt", "r") as inp_fp:
    k, d = [int(inp) for inp in inp_fp.readline().strip().split()]
    paired_reads = []
    while inp := inp_fp.readline().strip():
        paired_reads.append([element for element in inp.split("|") if element])

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


# Modified algo from tasks 11/13
def find_eulerian_path():
    # print(graph)
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
    # Rudementary
    # if len(path) >= len(graph):
    #     return reversed(path)
    return reversed(path)

eulerian_path = list(find_eulerian_path())

prefix_patterns = [n for n, _ in eulerian_path]
prefix_string = prefix_patterns[0]
for i in range(1, len(prefix_patterns)):
    prefix_string += prefix_patterns[i][-1]

suffix_patterns = [m for _, m in eulerian_path]
suffix_string = suffix_patterns[0]
for i in range(1, len(suffix_patterns)):
    suffix_string += suffix_patterns[i][-1]

answer = None
for i in range((k + d + 1), len(prefix_string)):
    if prefix_string[i] != suffix_string[i - k - d]:
        answer = ""
        break

if answer != "":
    answer = prefix_string + suffix_string[-k - d:]
print(answer)

with open("15_output.txt", "w+") as out_fp:
    out_fp.write(answer)
