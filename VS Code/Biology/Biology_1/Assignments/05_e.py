def find_clumps(dna_string, k, L, t):
    clumps = set()
    kmer_count = {}

    for i in range(len(dna_string) - k + 1):
        kmer = dna_string[i:i + k]

        if kmer in kmer_count:
            kmer_count[kmer] += 1
        else:
            kmer_count[kmer] = 1

        if kmer_count[kmer] >= t and kmer not in clumps:
            clumps.add(kmer)

        if i >= L - k:
            first_kmer = dna_string[i - L + k:i - L + 2 * k]
            kmer_count[first_kmer] -= 1
            if kmer_count[first_kmer] == 0:
                del kmer_count[first_kmer]

    return clumps

dna_string = "CGGACTCGACAGATGTGAAGAAATGTGAAGAAGGTGAAGAGGTCGAGTGTGAAGAAGTGAAGAAAGGTCGAAAGGTCGAGAAGGTGAAGAAGTGAAGAGG"
k = 9  
L = 500  
t = 3  

clumps = find_clumps(dna_string, k, L, t)

print(f"Patterns forming clumps of at least {t} occurrences in a {k}-mer of length {L}:\n{clumps}")
