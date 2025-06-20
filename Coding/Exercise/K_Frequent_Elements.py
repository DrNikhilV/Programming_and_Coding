def top_k_frequent(nums, k):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    freq = sorted(freq.items(), key=lambda x: -x[1])
    return [x[0] for x in freq[:k]]

print(top_k_frequent([1,1,1,2,2,3], 2))