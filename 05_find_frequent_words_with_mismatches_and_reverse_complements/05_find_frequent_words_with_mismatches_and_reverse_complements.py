with open("05_input.txt") as inp_fp:
    string = inp_fp.readline().strip()
    k, d = [int(entry) for entry in inp_fp.readline().strip().split()]

REVERSE_MAP = {
    'A': 'T',
    'T': 'A',
    'G': 'C',
    'C': 'G'
}

BUILDER_MAP = {
    0: 'A',
    1: 'T',
    2: 'G',
    3: 'C'
}


def get_pattern_occurences_count(pattern):
    answer = 0
    for i in range(0, len(string) - len(pattern) + 1):
        substr = string[i:i+len(pattern)]
        difference = 0
        for j, s in enumerate(pattern):
            if substr[j] != s:
                difference += 1
        if difference <= d:
            answer += 1
    return answer


def get_reversed_pattern(pattern):
    return ''.join([REVERSE_MAP[entry] for entry in reversed(pattern)])


def get_pattern_by_code(code):
    pattern = []
    for _ in range(k):
        pattern.append(BUILDER_MAP[code % 4])
        code //= 4
    return "".join(pattern)


answers = set()
max_count = -1
for i in range(4**k):
    pattern = get_pattern_by_code(i)
    # print(pattern, get_reversed_pattern(pattern))
    count = get_pattern_occurences_count(pattern) + get_pattern_occurences_count(get_reversed_pattern(pattern))
    if count > max_count:
        answers = {pattern, get_reversed_pattern(pattern)}
        max_count = count
    elif count == max_count:
        answers.add(pattern)
        answers.add(get_reversed_pattern(pattern))

print(answers)
with open("05_output.txt", "w+") as out_fp:
    out_fp.write(" ".join(answers))
