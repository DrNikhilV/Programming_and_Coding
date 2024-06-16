def replicate_dna(dna_strand):
    base_pairs = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C'}

    complementary_strand = ''

    for base in dna_strand:
        if base in base_pairs:
            complementary_strand += base_pairs[base]
        else:
            print(f"Invalid base '{base}' found.")
            return None

    return complementary_strand

with open("dna.txt", "r") as input1:
    input_DNA = input1.read()

complementary_strand = replicate_dna(input_DNA)

if complementary_strand:
    print(f"Complementary strand: {complementary_strand}")
