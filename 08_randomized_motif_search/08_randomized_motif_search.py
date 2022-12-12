import random

with open("08_input.txt") as inp_fp:
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

ITERATION_COUNT = 1000
ADDED_CONST = 1


def calculate_prob(profile, kmer):
    prob = 1.0
    for pos, el in enumerate(kmer):
        prob *= profile[MAP[el]][pos]
    return prob


def get_random_kmer(line):
    start_index = int(random.random() * len(line)) % (len(line) - k + 1)
    # print(start_index)
    return line[start_index:start_index + k]


def get_most_probable_kmer(profile, line):
    cur_max_prob = 0.0
    cur_max_kmer = line[0: len(profile[0])]
    for i in range(0, len(line) - len(profile[0]) + 1):
        kmer = line[i:i + k]
        cur_prob = calculate_prob(profile, kmer)
        if cur_prob > cur_max_prob:
            cur_max_prob = cur_prob
            cur_max_kmer = kmer
        elif cur_prob == cur_max_prob and random.random() > 0.5:
            cur_max_prob = cur_prob
            cur_max_kmer = kmer
    return cur_max_kmer


def get_count_matrix(motifs):
    count_matrix = [[], [], [], []]
    for i in range(len(motifs[0])):
        for nucleotid in range(len(MAP)):
            count_matrix[nucleotid].append(0)
        for j in range(len(motifs)):
            count_matrix[MAP[motifs[j][i]]][i] += 1
    for i in range(len(count_matrix)):
        for j in range(len(count_matrix[i])):
            count_matrix[i][j] += ADDED_CONST
    return count_matrix


def get_profile(motifs):
    count_matrix = get_count_matrix(motifs)
    all_sum = sum([count_matrix[j][0] for j in range(len(MAP))])
    # print(all_sum)
    for i in range(len(count_matrix)):
        for j in range(len(count_matrix[i])):
            count_matrix[i][j] /= all_sum
    return count_matrix


def get_score(motifs):
    count_matrix = get_count_matrix(motifs)
    score = 0
    for i in range(len(count_matrix[0])):
        max_count = max([count_matrix[j][i] for j in range(len(MAP))])
        all_sum = sum([count_matrix[j][i] for j in range(len(MAP))])
        score += all_sum - max_count
    return score


if len(matrix[0]) > k:
    current_best_score = None
    current_best_motifs = None

    for iteration in range(ITERATION_COUNT):
        motifs = []
        for i in range(len(matrix)):
            motifs.append(get_random_kmer(matrix[i]))
        best_iteration_motifs = None
        best_iteration_score = None
        while True:
            profile = get_profile(motifs)
            motifs = []
            for i in range(len(matrix)):
                motifs.append(get_most_probable_kmer(profile, matrix[i]))
            score = get_score(motifs)
            if best_iteration_motifs is None or score < best_iteration_score:
                best_iteration_score = score
                best_iteration_motifs = motifs
            else:
                break
        if current_best_score is None or best_iteration_score < current_best_score:
            print(iteration)
            current_best_score = best_iteration_score
            current_best_motifs = best_iteration_motifs

    print("Best score: ", current_best_score)
    answer = '\n'.join(current_best_motifs)
    with open("08_output.txt", "w+") as out_fp:
        out_fp.write(answer)
