from collections import defaultdict, OrderedDict

with open("18_input.txt") as inp_fp:
    spectrum = [int(entry) for entry in inp_fp.readline().strip().split()]

parent_mass = max(spectrum)
given_spectrum_dict = defaultdict(lambda: 0)
for entry in spectrum:
    given_spectrum_dict[entry] += 1

# Duplicates are not needed for the algo and were left for theoretical correctness
standard_mass_table = [
    # https://rosalind.info/problems/ba4c/
    # G  A   S   P   V   T    C    I    L    N    D    K    Q    E    M    H    F    R    Y    W
    57, 71, 87, 97, 99, 101, 103, 113, 113, 114, 115, 128, 128, 129, 131, 137, 147, 156, 163, 186
]

standard_masses_set = set(standard_mass_table)


class Peptide(list):
    def format(self):
        return "-".join([str(entry) for entry in self])

    def __hash__(self):
        if not self:
            return 0
        else:
            return hash("-".join([str(entry) for entry in self]))

    def __add__(self, *args, **kwargs):
        return Peptide(super().__add__(*args, **kwargs))


def linear_spectrum(peptide: Peptide):
    prefix = 0
    spectrum = defaultdict(lambda: 0)
    for i in range(len(peptide)):
        if i != 0:
            prefix += peptide[i - 1]
        inner_prefix = prefix
        for j in range(i + 1, len(peptide)):
            inner_prefix += peptide[j]
            spectrum[inner_prefix - prefix] += 1
    return spectrum


def cyclic_spectrum(peptide: Peptide):
    peptide_mass = sum(peptide)
    spectrum = defaultdict(lambda: 0)
    spectrum[0] = 1
    prefix = 0
    for i in range(len(peptide)):
        if i != 0:
            prefix += peptide[i - 1]
        inner_prefix = prefix
        for j in range(i + 1, len(peptide) + 1):
            inner_prefix += peptide[j - 1]
            spectrum[inner_prefix - prefix] += 1
            # Cycle
            if i > 0 and j < len(peptide):
                spectrum[peptide_mass - (inner_prefix - prefix)] += 1
    return spectrum


peptides = {Peptide()}
result = []
while len(peptides) > 0:
    new_peptides = set()
    for peptide in peptides:
        for mass in sorted(standard_masses_set):
            new_peptides.add(peptide + Peptide([mass]))
    peptides = new_peptides
    deletions = []

    new_peptides = peptides.copy()
    for peptide in peptides:
        mass = sum(peptide)
        if mass == parent_mass:
            if cyclic_spectrum(peptide) == given_spectrum_dict:
                result.append(peptide.format())
            print(result)
            new_peptides.remove(peptide)
        else:
            is_consistent = True
            for key, value in linear_spectrum(peptide).items():
                if value > given_spectrum_dict.get(key, 0):
                    is_consistent = False
                    break
            if not is_consistent:
                new_peptides.remove(peptide)
    peptides = new_peptides

print(result)

with open("18_output.txt", "w+") as out_fp:
    out_fp.write(" ".join(result))
