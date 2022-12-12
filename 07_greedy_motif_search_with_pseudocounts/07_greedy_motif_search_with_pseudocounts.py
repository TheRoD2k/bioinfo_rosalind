with open("07_input.txt") as inp_fp:
    k, t = [int(p) for p in inp_fp.readline().strip().split()]
    matrix = []
    for i in range(0, t):
        matrix.append(inp_fp.readline().strip())

MAP = {
    "A": 0,
    "C": 1,
    "G": 2,
    "T": 3
}


def calculate_prob(profile, kmer):
    prob = 1.0
    for pos, el in enumerate(kmer):
        prob *= profile[MAP[el]][pos]
    return prob


def get_most_probable_kmer(profile, line):
    cur_max_prob = 0.0
    cur_max_kmer = line[0: len(profile[0])]
    for i in range(0, len(line) - len(profile[0]) + 1):
        kmer = line[i:i + len(profile[0])]
        cur_prob = calculate_prob(profile, kmer)
        if cur_prob > cur_max_prob:
            cur_max_prob = cur_prob
            cur_max_kmer = kmer
    return cur_max_kmer


def get_count_matrix(motifs):
    count_matrix = [[], [], [], []]
    for i in range(len(motifs[0])):
        for nucleotid in range(len(MAP)):
            count_matrix[nucleotid].append(0)
        for j in range(len(motifs)):
            # print(motifs)
            # print(t)
            # print(count_matrix)
            # print(i, j, count_matrix)
            count_matrix[MAP[motifs[j][i]]][i] += 1
    for i in range(len(count_matrix)):
        for j in range(len(count_matrix[i])):
            count_matrix[i][j] += 1
    return count_matrix


def get_profile(motifs):
    count_matrix = get_count_matrix(motifs)
    for i in range(len(count_matrix)):
        for j in range(len(count_matrix[i])):
            count_matrix[i][j] /= (2 * t)
    return count_matrix


def get_score(motifs):
    count_matrix = get_count_matrix(motifs)
    score = 0
    for i in range(len(count_matrix[0])):
        max_count = max([count_matrix[j][i] for j in range(len(MAP))])
        score += t - max_count
    return score


if len(matrix[0]) > k:
    current_best_score = t * len(matrix[0]) + 1
    current_best_motifs = None
    for i in range(0, len(matrix[0]) - k + 1):
        motif_0 = matrix[0][i:i + k]
        motifs = [motif_0]

        for j in range(1, t):
            profile = get_profile(motifs)
            kmer = get_most_probable_kmer(profile, matrix[j])
            motifs.append(kmer)
        profile = get_profile(motifs)
        score = get_score(motifs)
        if score < current_best_score:
            current_best_score = score
            current_best_motifs = motifs


answer = '\n'.join(current_best_motifs)
with open("07_output.txt", "w+") as out_fp:
    out_fp.write(answer)
