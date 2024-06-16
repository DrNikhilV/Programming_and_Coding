def reverse_complement(dna_string):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reverse_comp = [complement[base] for base in dna_string[::-1]]
    return ''.join(reverse_comp)

dna_string = "ATCGTAGCAT"
reverse_comp = reverse_complement(dna_string)

print(f"Original DNA String: {dna_string}")
print(f"Reverse Complement: {reverse_comp}")
