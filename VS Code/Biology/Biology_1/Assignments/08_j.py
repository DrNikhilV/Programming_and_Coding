from collections import Counter

def hamming_distance(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

def reverse_complement(pattern):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in pattern[::-1])

def find_frequent_with_mismatches_and_reverse_complements(text, k, d):
    frequent_words = []
    max_count = 0
    kmer_count = Counter()

    for i in range(len(text) - k + 1):
        kmer = text[i:i + k]
        rev_kmer = reverse_complement(kmer)
        for neighbor in generate_neighbors(kmer, d):
            kmer_count[neighbor] += 1
            if kmer_count[neighbor] > max_count:
                max_count = kmer_count[neighbor]
                frequent_words = [neighbor]
            elif kmer_count[neighbor] == max_count:
                frequent_words.append(neighbor)
        
        for neighbor in generate_neighbors(rev_kmer, d):
            kmer_count[neighbor] += 1
            if kmer_count[neighbor] > max_count:
                max_count = kmer_count[neighbor]
                frequent_words = [neighbor]
            elif kmer_count[neighbor] == max_count:
                frequent_words.append(neighbor)

    return frequent_words, max_count

def generate_neighbors(pattern, d):
    if d == 0:
        return [pattern]
    if len(pattern) == 1:
        return ['A', 'C', 'G', 'T']

    neighbors = []
    suffix_neighbors = generate_neighbors(pattern[1:], d)
    for neighbor in suffix_neighbors:
        if hamming_distance(neighbor, pattern[1:]) < d:
            for nucleotide in 'ACGT':
                neighbors.append(nucleotide + neighbor)
        else:
            neighbors.append(pattern[0] + neighbor)

    return neighbors

text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4  
d = 1  

frequent_words, max_count = find_frequent_with_mismatches_and_reverse_complements(text, k, d)

print(f"Most frequent {k}-mers with at most {d} mismatches and their reverse complements:")
for word in frequent_words:
    print(f"{word} (and its reverse complement {reverse_complement(word)}): {max_count} times")
