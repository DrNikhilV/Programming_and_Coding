#Number of Arithmetic Triplets

def arithmetic_triplets(nums, diff):
    # Set to store the numbers we have seen
    seen = set()
    count = 0
    
    for num in nums:
        # Check if the current number can form a valid triplet
        if (num - diff in seen) and (num - 2 * diff in seen):
            count += 1
        # Add the current number to the set
        seen.add(num)
    
    return count

# Example usage
nums = [0, 1, 4, 6, 7, 10]
diff = 3
result = arithmetic_triplets(nums, diff)
print("Number of arithmetic triplets:", result)
