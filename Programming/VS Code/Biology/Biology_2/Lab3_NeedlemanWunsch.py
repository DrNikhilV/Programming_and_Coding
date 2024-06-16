# Needleman Wunsch Algorithm
seq1 = "ATGCA"
seq2 = "AGCA"

m = 2
miss = -1
gap = -2

l1, l2 = len(seq1), len(seq2)

score = [[0] * (l2 + 1) for _ in range(l1 + 1)]

for i in range(1, l1 + 1):
    score[i][0] = i * gap
for j in range(1, l2 + 1):
    score[0][j] = j * gap

for i in range(1, l1 + 1):
    for j in range(1, l2 + 1):
        match = score[i - 1][j - 1] + (m if seq1[i - 1] == seq2[j - 1] else miss)
        delete = score[i - 1][j] + gap
        insert = score[i][j - 1] + gap
        score[i][j] = max(match, delete, insert)

print("Resultant Scoring Matrix:")
for row in score:
    print(row)

align_seq1, align_seq2 = "", ""
i, j = l1, l2
alignment_score = 0 

while i > 0 or j > 0:
    current = score[i][j]
    diag = score[i - 1][j - 1] if i > 0 and j > 0 else float('-inf')
    vert = score[i - 1][j] if i > 0 else float('-inf')
    hori = score[i][j - 1] if j > 0 else float('-inf')

    if current == diag + (m if seq1[i - 1] == seq2[j - 1] else miss):
        align_seq1 = seq1[i - 1] + align_seq1
        align_seq2 = seq2[j - 1] + align_seq2
        i -= 1
        j -= 1
        alignment_score += (m if seq1[i] == seq2[j] else miss)
    elif current == vert + gap:
        align_seq1 = seq1[i - 1] + align_seq1
        align_seq2 = "-" + align_seq2
        i -= 1
        alignment_score += gap
    else:
        align_seq1 = "-" + align_seq1
        align_seq2 = seq2[j - 1] + align_seq2
        j -= 1
        alignment_score += gap

print("\nAligned Sequences:")
print("Sequence 1:", align_seq1)
print("Sequence 2:", align_seq2)
print("Alignment Score:", alignment_score)
