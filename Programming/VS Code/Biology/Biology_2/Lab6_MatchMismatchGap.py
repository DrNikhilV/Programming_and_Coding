def alignment_score(seq1, seq2, match_score, mismatch_score, gap_penalty):
    score = 0
    for i in range(len(seq1)):
        if seq1[i] == '-' or seq2[i] == '-':
            score += gap_penalty
        elif seq1[i] == seq2[i]:
            score += match_score
        else:
            score += mismatch_score
    return score


aligned_seq1 = input("Enter first aligned sequence: ")#gaattc-a
aligned_seq2 = input("Enter second aligned sequence: ")#ggat-cga
match_score = int(input("Enter match score: "))#2
mismatch_score = int(input("Enter mismatch score: "))#-1
gap_penalty = int(input("Enter gap penalty: "))#-2
    
score = alignment_score(aligned_seq1, aligned_seq2, match_score, mismatch_score, gap_penalty)
    
print(f"Alignment score: {score}")

