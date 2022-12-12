with open("01_input.txt", "r") as inp_fp:
    pattern = inp_fp.readline().strip()
    data = inp_fp.readline().strip()
# Could use re.findall here, but result is prone to errors for certain import data formats
# import re
# for entry_pos in [match.start() for match in re.finditer(rf"(?={pattern})", data)]:
#     print(entry_pos, end=" ")
# print()

if not (not pattern or not data or len(pattern) > len(data)):
    found_pos = []
    temp = ""
    for i in range(0, len(data) - len(pattern) + 1):
        if data[i:i + len(pattern)] == pattern:
            found_pos.append(i)

    answer = ' '.join([str(pos) for pos in found_pos])
    with open("01_output.txt", "a+") as out_fp:
        out_fp.write(answer)
