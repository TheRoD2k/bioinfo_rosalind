with open("02_input.txt", "r") as inp_fp:
    data = inp_fp.readline().strip()
    k, l, t = [int(inp.strip()) for inp in inp_fp.readline().split()]

patterns = set()

if not len(data) < k:
    entries = {}
    previous_substr = None
    for i in range(0, len(data) - k + 1):
        current_substr = data[i:i + k]
        if len(current_substr) < k:
            continue

        entries[current_substr] = entries.get(current_substr, 0) + 1
        if entries[current_substr] >= t:
            patterns.add(current_substr)
        previous_substr = data[i + k - l - 2: i + k - l - 2 + k]
        if i >= l:
            entries[previous_substr] -= 1

answer = ' '.join(patterns)
with open("02_output.txt", "w+") as out_fp:
    out_fp.write(answer)
