from collections import defaultdict

with open("27_input.txt") as inp_fp:
    genomes = [[], []]
    for i in range(2):
        entries = inp_fp.readline().strip().split(")(")
        singular = []
        for entry in entries:
            if entry[0] == "(":
                entry = entry[1:]
            if entry[-1] == ")":
                entry = entry[:-1]
            singular.append([int(num) for num in entry.split()])
        genomes[i].extend(singular)


def colored_edges(genome):
    edges = set()
    for chromosome in genome:
        nodes = [0] * (2 * len(chromosome))
        for pos in range(len(chromosome)):
            el = chromosome[pos]
            nodes[2 * pos] = (2 * el - 1) if el > 0 else (-2 * el)
            nodes[2 * pos + 1] = (2 * el) if el > 0 else (-2 * el - 1)
        nodes.append(nodes[0])
        for pos in range(len(chromosome)):
            edges.add((nodes[2 * pos + 1], nodes[2 * pos + 2]))
    return edges


edges = colored_edges(genomes[0]) | (colored_edges(genomes[1]))
parent = defaultdict(lambda x: x)

for edge in edges:
    parent[edge[0]] = edge[0]
    parent[edge[1]] = edge[1]


def get_parent(node):
    while node != parent[node]:
        node = parent[node]
    return node


rank = defaultdict(lambda: 0)
for edge in edges:
    if (left_parent := get_parent(edge[0])) == (right_parent := get_parent(edge[1])):
        continue
    if rank[left_parent] > rank[right_parent]:
        parent[right_parent] = left_parent
    else:
        parent[left_parent] = right_parent
        if rank[left_parent] == rank[right_parent]:
            rank[right_parent] += 1

nodes = {get_parent(edge[0]) for edge in edges}
answer = str(sum([len(g) for g in genomes[0]]) - len(nodes))

with open("27_output.txt", "w+") as out_fp:
    out_fp.write(answer)
