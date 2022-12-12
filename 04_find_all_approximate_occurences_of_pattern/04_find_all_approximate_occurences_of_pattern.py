with open("04_input.txt") as inp_fp:
    pattern = inp_fp.readline().strip()
    string = inp_fp.readline().strip()
    d = int(inp_fp.readline().strip())

answer = []
for i in range(0, len(string) - len(pattern) + 1):
    substr = string[i:i+len(pattern)]
    difference = 0
    for j, s in enumerate(pattern):
        if substr[j] != s:
            difference += 1
    if difference <= d:
        answer.append(str(i))

with open("04_output.txt", "w+") as out_fp:
    out_fp.write(" ".join(answer))
