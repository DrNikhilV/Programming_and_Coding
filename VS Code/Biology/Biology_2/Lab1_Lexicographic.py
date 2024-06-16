#Lab 1- Form 3-mers from above sequence sequence (last sem lab exercise) and write a python code to arrange them 
#lexicographically.

sequence = "ATAGGCTACATGCG"
l = len(sequence)

k = int(input("Enter Kmer Length : "))

print("Kmers of length 2")
kmers = [sequence[i:i+k] for i in range(l - k + 1)]
print("Before Sorting : ")
print(kmers)
kmers.sort()
print("After Sorting : ")
print(kmers)
print()
