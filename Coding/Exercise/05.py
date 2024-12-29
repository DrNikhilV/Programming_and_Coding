#Find the Number of Good Pairs I

#BruteForce
def num_identical_pairs(nums):
    count = 0
    
    # Loop through all possible pairs (i, j)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                count += 1
    
    return count

nums = [1, 2, 3, 1, 1, 3]
result = num_identical_pairs(nums)
print("Number of good pairs:", result)

#Optimised
def num_identical_pairs(nums):
    freq = {}
    count = 0
    
    # Count the frequency of each number
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    # Calculate the number of good pairs based on frequency
    for f in freq.values():
        if f > 1:
            count += (f * (f - 1)) // 2
    
    return count

# Example usage
nums = [1, 2, 3, 1, 1, 3]
result = num_identical_pairs(nums)
print("Number of good pairs:", result)