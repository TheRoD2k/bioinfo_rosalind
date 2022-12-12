with open("17_input.txt") as inp_fp:
    total_mass = int(inp_fp.readline().strip())

# Duplicates are not needed for the algo and were left for theoretical correctness
standard_mass_table = [
    # https://rosalind.info/problems/ba4c/
    # G  A   S   P   V   T    C    I    L    N    D    K    Q    E    M    H    F    R    Y    W
    57, 71, 87, 97, 99, 101, 103, 113, 113, 114, 115, 128, 128, 129, 131, 137, 147, 156, 163, 186
]

standard_masses_set = set(standard_mass_table)

possible_by_mass = [(0 if i not in standard_masses_set else 1) for i in range(total_mass + 1)]

for mass in range(total_mass + 1):
    for mass_to_add in standard_masses_set:
        if mass_to_add > mass:
            continue
        possible_by_mass[mass] += possible_by_mass[mass - mass_to_add]

with open("17_output.txt", "w+") as out_fp:
    out_fp.write(str(possible_by_mass[total_mass]))
