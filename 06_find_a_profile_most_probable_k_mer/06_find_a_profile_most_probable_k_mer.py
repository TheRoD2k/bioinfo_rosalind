with open("06_input.txt") as inp_fp:
    data = inp_fp.readline().strip()
    k = int(inp_fp.readline().strip())
    matrix = []
    for i in range(0, 4):
        matrix.append([float(p.strip()) for p in inp_fp.readline().split()])
    assert len(matrix[0]) == k

max_prob = 0.0
max_prob_k_mer = ""
MAP = {
    "A": 0,
    "C": 1,
    "G": 2,
    "T": 3
}

if len(data) > k:
    for i in range(0, len(data) - k + 1):
        substr = data[i:i + k]

        prob = 1.0
        for j in range(0, len(substr)):
            prob *= matrix[MAP[substr[j]]][j]
        print(substr, prob)
        if prob > max_prob:
            max_prob = prob
            max_prob_k_mer = substr

with open("06_output.txt", "w+") as out_fp:
    out_fp.write(max_prob_k_mer)
