from collections import defaultdict

with open("03_input.txt", "r") as inp_fp:
    data = inp_fp.readline().strip()

operation = defaultdict(lambda: 0)
operation.update({"C": -1, "G": 1})
entries = defaultdict(list)
entries.update({0: ["0"]})
value = 0
for i in range(1, len(data) + 1):
    value += operation[data[i - 1]]
    entries[value].append(str(i))

min_value = min(entries.keys())
answer = ' '.join(entries[min_value])
with open("03_output.txt", "w+") as out_fp:
    out_fp.write(answer)
