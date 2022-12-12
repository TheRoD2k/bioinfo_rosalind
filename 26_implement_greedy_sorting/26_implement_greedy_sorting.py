with open("26_input.txt") as inp_fp:
    sequence = [int(entry) for entry in inp_fp.readline().strip()[1:-1].split()]

print(sequence)

history = []


def find_min(from_pos, to_pos):
    min_pos = -1
    min_abs = max([abs(entry) for entry in sequence])
    for i in range(from_pos, to_pos):
        if abs(sequence[i]) <= min_abs:
            min_abs = abs(sequence[i])
            min_pos = i
    return min_pos, min_abs


for i in range(len(sequence)):
    # Can use k-sort (which is even simpler and faster) if permutations
    # are formed by first positive integers
    # (As it is actually written in the task, but I am dumb...)
    min_pos, min_abs = find_min(i, len(sequence))
    if min_abs != abs(sequence[i]):
        sequence = sequence[:i] + [-e for e in reversed(sequence[i:min_pos + 1])] + sequence[min_pos + 1:]
        history.append(sequence.copy())
    min_pos, min_abs = find_min(i, len(sequence))
    if min_abs == -sequence[i]:
        sequence[i] = abs(sequence[i])
        history.append(sequence.copy())

print(history)

formatted_string = ["(" + " ".join([f"+{num}" if num > 0 else str(num) for num in entry]) + ")" for entry in history]
answer = "\n".join(formatted_string)
with open("26_output.txt", "w+") as out_fp:
    out_fp.write(answer)
