from collections import defaultdict

SCORING_MATRIX = defaultdict(lambda: defaultdict(lambda: 0))
PENALTY = 5

# I would die if I try to hardcode it
with open("table.txt") as table_fp:
    letters = table_fp.readline().strip().split()
    for _ in range(len(letters)):
        row = table_fp.readline().strip().split()
        row_letter = row[0]
        for col_letter, score in zip(letters, row[1:]):
            SCORING_MATRIX[row_letter][col_letter] = int(score)

with open("23_input.txt") as inp_fp:
    string_1 = inp_fp.readline().strip()
    string_2 = inp_fp.readline().strip()


cols = len(string_1) + 1
rows = len(string_2) + 1
scores = [[-(i or j) * PENALTY if i * j == 0 else 0 for i in range(cols)] for j in range(rows)]

print(scores[0])
for i in range(rows - 1):
    for j in range(cols - 1):
        letter_1 = string_1[j]
        letter_2 = string_2[i]
        scores[i + 1][j + 1] = max(
            0,
            scores[i][j + 1] - PENALTY,
            scores[i + 1][j] - PENALTY,
            scores[i][j] + SCORING_MATRIX[letter_2][letter_1]
        )
print(scores[1])
max_score = 0
for i in range(rows):
    for j in range(cols):
        if max_score < scores[i][j]:
            max_score = scores[i][j]
            max_score_row = i - 1
            max_score_col = j - 1

print(max_score)
print(max_score_col)
print(max_score_row)


answer_1 = []
answer_2 = []
score_row = max_score_row
score_col = max_score_col
current_score = None

while (current_score is None or current_score != 0) and (score_row > 0 or score_col > 0):
    letter_1 = string_1[score_col]
    letter_2 = string_2[score_row]
    current_score = scores[score_row + 1][score_col + 1] - SCORING_MATRIX[letter_2][letter_1]
    if current_score == scores[score_row][score_col]:
        answer_1.append(letter_1)
        answer_2.append(letter_2)
        score_row -= 1
        score_col -= 1
    elif scores[score_row + 1][score_col] > scores[score_row][score_col + 1]:
        answer_1.append(letter_1)
        answer_2.append("-")
        current_score = scores[score_row + 1][score_col]
        score_col -= 1
    else:
        answer_1.append("-")
        answer_2.append(letter_2)
        current_score = scores[score_row][score_col + 1]
        score_row -= 1

answer_1 = "".join(reversed(answer_1))
answer_2 = "".join(reversed(answer_2))
answer = "\n".join([str(max_score), answer_1, answer_2])

with open("23_output.txt", "w+") as out_fp:
    out_fp.write(answer)
