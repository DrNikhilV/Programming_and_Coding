#Lab 2- start with a random 3-mer and do string reconstruction using prefix and suffix. Write python code for it. 
#Do minimum 10 runs to see if you get the original sequence. Print the consensus sequence in each test run. 
#How many iterations are required to actually reconstruct the original sequence.

import random

seq = "ATAGGCTACATGCG"
l = len(seq)
k = 3
i = 0

kmers1 = [seq[i:i+k] for i in range(l - k + 1)]

kmers1.sort()
print(kmers1)

kmers2 = kmers1

sequence = kmers1[random.randint(0, len(kmers1) - 1)]
print(sequence)
kmers2.remove(sequence)

for i in range(20):
    t = False

    for kmer in kmers2:
        if sequence[-k + 1:] == kmer[:k - 1]:
            sequence += kmer[-1]
            kmers2.remove(kmer)
            t = True
            i+=1
            break

        if sequence[:k - 1] == kmer[1:]:
            sequence = kmer[0] + sequence
            kmers2.remove(kmer)
            t = True
            i+=1
            break

    if not t:
        break

    print(sequence, end=" , ")
print("Iterations: ",i)