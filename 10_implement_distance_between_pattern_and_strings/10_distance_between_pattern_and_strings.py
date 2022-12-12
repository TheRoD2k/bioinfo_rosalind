with open("10_input.txt") as inp_fp:
    pattern = inp_fp.readline().strip()
    dna = inp_fp.readline().strip().split()

INF = 1e9
k = len(pattern)
distance = 0

for string in dna:
    hamming_distance = INF
    for i in range(len(string) - k + 1):
        kmer = string[i:i + k]
        difference = 0
        for j, s in enumerate(kmer):
            if pattern[j] != s:
                difference += 1
        if hamming_distance > difference:
            hamming_distance = difference
    distance = distance + hamming_distance

print(distance)

with open("10_output.txt", "w+") as out_fp:
    out_fp.write(str(distance))
