with open("12_input.txt", "r") as inp_fp:
    k = int(inp_fp.readline().strip())

# This task broke my brain, so I looked for the idea of constructing
# DeBruijn sequence on Wiki, understood nothing and went further for
# Frank Ruskey's "Combinatorial Generation".
# May the God forgive me.
# Basically it is a modification of FKM algorithm (suitable for necklaces)
# Citation from the book:
    # The idea is to successively concatenate the reduction of each necklace as it is produced by
    # the FKM algorithm. Thus we are concatenating all Lyndon words of length divisible by k
    # in lexicographic order.
ALPHABET_SIZE = 2

if k > 0:
    alphabet = [str(i) for i in range(ALPHABET_SIZE)]
    a = [0] * ALPHABET_SIZE * k
    string = []

    def fkm(t, p):
        if t > k:
            # PrintIn function representation for DeBruijn sequence
            if k % p == 0:
                string.extend(a[1: p + 1])
        else:
            a[t] = a[t - p]
            fkm(t + 1, p)
            for j in range(a[t - p] + 1, ALPHABET_SIZE):
                a[t] = j
                fkm(t + 1, t)
    fkm(1, 1)

    with open("12_output.txt", "w+") as out_fp:
        out_fp.write("".join([alphabet[i] for i in string]))
