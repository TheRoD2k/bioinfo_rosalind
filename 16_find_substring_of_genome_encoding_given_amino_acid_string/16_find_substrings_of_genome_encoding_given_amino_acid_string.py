with open("16_input.txt", "r") as inp_fp:
    dna = inp_fp.readline().strip()
    peptide = inp_fp.readline().strip()

SEQ_LEN = len(peptide) * 3
# Hard-code the codon table
BASE_MAP = [
    (["UUU", "UUC"], "F"),
    (["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"], "L"),
    (["AUU", "AUC", "AUA"], "I"),
    (["AUG"], "M"),
    (["GUU", "GUC", "GUA", "GUG"], "V"),
    (["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"], "S"),
    (["CCU", "CCC", "CCA", "CCG"], "P"),
    (["ACU", "ACC", "ACA", "ACG"], "T"),
    (["GCU", "GCC", "GCA", "GCG"], "A"),
    (["UAU", "UAC"], "Y"),
    (["UAA", "UAG", "UGA"], "STOP"),  # STOP CODON
    (["CAU", "CAC"], "H"),
    (["CAA", "CAG"], "Q"),
    (["AAU", "AAC"], "N"),
    (["AAA", "AAG"], "K"),
    (["GAU", "GAC"], "D"),
    (["GAA", "GAG"], "E"),
    (["UGU", "UGC"], "C"),
    (["UGG"], "W"),
    (["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"], "R"),
    (["GGU", "GGC", "GGA", "GGG"], "G")
]

MAP = {}
for element in BASE_MAP:
    for base in element[0]:
        MAP[base] = element[1]

# Check correctness
for first_base in ["U", "C", "A", "G"]:
    for second_base in ["U", "C", "A", "G"]:
        for third_base in ["U", "C", "A", "G"]:
            base = f"{first_base}{second_base}{third_base}"
            assert base in MAP, f"{base} is not in the map"
values = {
    "F",
    "L",
    "I",
    "V",
    "M",
    "S",
    "P",
    "T",
    "A",
    "Y",
    "H",
    "Q",
    "N",
    "K",
    "D",
    "E",
    "C",
    "W",
    "R",
    "G",
    "STOP"
}
assert values == set(MAP.values()), values.difference(MAP.values())


def get_rna_sequence(dna):
    return ''.join(["U" if c == "T" else c for c in dna])


rna = get_rna_sequence(dna)
positions = set()
for i in range(len(dna) - SEQ_LEN + 1):
    temp = []
    for j in range(i, i + SEQ_LEN, 3):
        temp.append(MAP[rna[j:j+3]])
    temp = ''.join(temp)
    print(temp)
    if temp == peptide:
        positions.add(i)

REVERSE_MAP = {
    'A': 'U',
    'U': 'A',
    'G': 'C',
    'C': 'G'
}

for i in range(len(dna) - SEQ_LEN):
    temp = []
    for j in range(i, i + SEQ_LEN, 3):
        reversed_codon = ''.join([REVERSE_MAP[nucleotid] for nucleotid in reversed(rna[j:j + 3])])
        # print(reversed_codon)
        temp.append(MAP[reversed_codon])
    temp = ''.join(reversed(temp))
    print(temp)
    if temp == peptide:
        positions.add(i)

output = "\n".join([dna[position: position + SEQ_LEN] for position in positions])
with open("16_output.txt", "w+") as out_fp:
    out_fp.write(output)
