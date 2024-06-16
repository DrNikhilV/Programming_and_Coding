def smith_waterman(seq1, seq2, m=2, mm=-1, g=-2):
    rows = len(seq1) + 1
    cols = len(seq2) + 1
    scores = [[0] * cols for _ in range(rows)]

    max_score = 0
    max_pos = (0, 0)

    for i in range(1, rows):
        for j in range(1, cols):
            if seq1[i-1] == seq2[j-1]:
                match = scores[i-1][j-1] + m
            else:
                match = scores[i-1][j-1] + mm

            u = scores[i-1][j] + g
            d = scores[i][j-1] + g

            scores[i][j] = max(0, match, u, d)

            if scores[i][j] > max_score:
                max_score = scores[i][j]
                max_pos = (i, j)

    s1 = ""
    s2 = ""
    i, j = max_pos
    while scores[i][j] != 0:
        if scores[i][j] == scores[i-1][j-1] + (m if seq1[i-1] == seq2[j-1] else mm):
            s1 = seq1[i-1] + s1
            s2 = seq2[j-1] + s2
            i -= 1
            j -= 1
        elif scores[i][j] == scores[i-1][j] + g:
            s1 = seq1[i-1] + s1
            s2 = '-' + s2
            i -= 1
        elif scores[i][j] == scores[i][j-1] + g:
            s1 = '-' + s1
            s2 = seq2[j-1] + s2
            j -= 1
    
    return max_score, s1, s2, scores

seq1 = "ACGTAGC"
seq2 = "ACGGTAG"
score, s1, s2, scores = smith_waterman(seq1, seq2)
print("Score:", score)
print("Sequence 1:", s1)
print("Sequence 2:", s2)