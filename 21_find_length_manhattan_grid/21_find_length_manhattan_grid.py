from collections import defaultdict

with open("21_input.txt") as inp_fp:
    n, m = [int(entry) for entry in inp_fp.readline().strip().split()]
    down = []
    while (line := inp_fp.readline().strip()) != "-":
        down.append([int(entry) for entry in line.split()])
    right = []
    while line := inp_fp.readline():
        right.append([int(entry) for entry in line.strip().split()])

assert len(down) == n
assert len(down[0]) == m + 1

assert len(right) == n + 1
assert len(right[0]) == m

s = defaultdict(lambda: defaultdict(lambda: 0))
for i in range(1, n + 1):
    s[i][0] = s[i - 1][0] + down[i - 1][0]
for j in range(1, m + 1):
    s[0][j] = s[0][j - 1] + right[0][j - 1]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        s[i][j] = max(s[i - 1][j] + down[i - 1][j], s[i][j - 1] + right[i][j - 1])

with open("21_output.txt", "w+") as out_fp:
    out_fp.write(str(s[n][m]))
