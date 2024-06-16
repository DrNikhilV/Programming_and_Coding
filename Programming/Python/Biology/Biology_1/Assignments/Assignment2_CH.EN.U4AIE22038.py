#Question 01
def most_probable_kmer(sequence, k):
    kmer_count = {}

    for i in range(len(sequence) - k + 1):
        kmer = sequence[i:i + k]
        if kmer in kmer_count:
            kmer_count[kmer] += 1
        else:
            kmer_count[kmer] = 1

    max_count = max(kmer_count.values())
    most_probable_kmers = [kmer for kmer, count in kmer_count.items() if count == max_count]

    return most_probable_kmers

sequence = "AGTACGGTACGTACGTTAGCTAGTGCATGTATACGTAGTACG"
k = 4
output = most_probable_kmer(sequence, k)
print("Most probable", k, "-mer(s):", output)

#Question 02

def find_motif_greedy(dna_sequences, k, t):
    best_motifs = [seq[:k] for seq in dna_sequences]
    for i in range(len(dna_sequences[0]) - k + 1):
        motif = dna_sequences[0][i:i + k]
        motifs = [motif]
        for j in range(1, t):
            profile = create_profile_matrix(motifs)
            next_motif = find_most_probable_kmer(dna_sequences[j], k, profile)
            motifs.append(next_motif)
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
    return best_motifs

def create_profile_matrix(motifs):
    profile = {'A': [], 'C': [], 'G': [], 'T': []}
    k = len(motifs[0])
    t = len(motifs)
    for i in range(k):
        col = [motif[i] for motif in motifs]
        for base in "ACGT":
            profile[base].append((col.count(base) + 1) / (t + 4))
    return profile

def find_most_probable_kmer(dna_string, k, profile):
    max_prob = -1
    most_probable_kmer = ""
    for i in range(len(dna_string) - k + 1):
        kmer = dna_string[i:i + k]
        probability = 1.0
        for j in range(k):
            probability *= profile[kmer[j]][j]
        if probability > max_prob:
            max_prob = probability
            most_probable_kmer = kmer
    return most_probable_kmer

def score(motifs):
    k = len(motifs[0])
    t = len(motifs)
    score = 0
    for i in range(k):
        col = [motif[i] for motif in motifs]
        most_common = max(col, key=col.count)
        score += t - col.count(most_common)
    return score

# Example usage:
dna_sequences = [
    "CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA",
    "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG",
    "TAGTACCGAGACCGAAAGAAGTATACAGGCGT",
    "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC",
    "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"
]

k = 8
t = len(dna_sequences)
best_motifs = find_motif_greedy(dna_sequences, k, t)
for motif in best_motifs:
    print(motif)


#Question 03

import numpy as np

def profile_most_probable_kmer(dna, k, profile):
    max_probability = -1
    most_probable_kmer = ""
    for i in range(len(dna) - k + 1):
        kmer = dna[i:i + k]
        probability = 1.0
        for j in range(k):
            if kmer[j] == "A":
                probability *= profile[0][j]
            elif kmer[j] == "C":
                probability *= profile[1][j]
            elif kmer[j] == "G":
                probability *= profile[2][j]
            elif kmer[j] == "T":
                probability *= profile[3][j]
        if probability > max_probability:
            max_probability = probability
            most_probable_kmer = kmer
    return most_probable_kmer

def profile_matrix_with_pseudocounts(motifs):
    k = len(motifs[0])
    profile = np.ones((4, k))
    for motif in motifs:
        for i in range(k):
            if motif[i] == "A":
                profile[0][i] += 1
            elif motif[i] == "C":
                profile[1][i] += 1
            elif motif[i] == "G":
                profile[2][i] += 1
            elif motif[i] == "T":
                profile[3][i] += 1
    profile = profile / (len(motifs) + 4)
    return profile

def greedy_motif_search_with_pseudocounts(sequences, k, t):
    best_motifs = [dna[:k] for dna in sequences]
    for i in range(len(sequences[0]) - k + 1):
        motifs = [sequences[0][i:i + k]]
        for j in range(1, t):
            profile = profile_matrix_with_pseudocounts(motifs)
            most_probable_kmer = profile_most_probable_kmer(sequences[j], k, profile)
            motifs.append(most_probable_kmer)
        if score_motifs(motifs) < score_motifs(best_motifs):
            best_motifs = motifs
    return best_motifs

def score_motifs(motifs):
    k = len(motifs[0])
    score = 0
    for i in range(k):
        count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for motif in motifs:
            count[motif[i]] += 1
        score += sum(count.values()) - max(count.values())
    return score

sequences = ["GGCGTTCAGGCA", "AAGAATCAGTCA", "CAAGGAGTTCGC", "CAATAATATTCG", "ATCGATGCAGTA"]
k = 3
t = 5
best_motifs = greedy_motif_search_with_pseudocounts(sequences, k, t)
for motif in best_motifs:
    print(motif)
