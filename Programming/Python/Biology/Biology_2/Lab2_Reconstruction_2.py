import random

dna = "ATAGGCTACATGCG"
knum = int(input("Enter k-mer length: "))
iterations = 25

kmer_list = []


for i in range(0, len(dna) - knum + 1):
    kmer_list.append(dna[i:i + knum])

kmer_list.sort()
print(kmer_list)

copy_kmer = [i for i in kmer_list]


sequence = kmer_list[random.randint(0, len(kmer_list) - 1)]
print(sequence)
copy_kmer.remove(sequence)
print(copy_kmer)
count_iterations = 0


for _ in range(iterations):
    found = False

   
    for kmer in copy_kmer:
        if sequence[-knum + 1:] == kmer[:knum - 1]:
            sequence += kmer[-1]
            copy_kmer.remove(kmer)
            found = True
            count_iterations += 1
            break

        if sequence[:knum - 1] == kmer[1:]:
            sequence = kmer[0] + sequence
            copy_kmer.remove(kmer)
            found = True
            count_iterations += 1
            break

    if not found:
        break

    print(sequence)
    print(copy_kmer)

print(f"Number of iterations: {count_iterations}")