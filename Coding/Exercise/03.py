#Sum of All Subset XOR Totals

def sum_of_subset_xor(arr):
    n = len(arr)
    total_xor_sum = 0
    max_bits = 32  # Considering 32 bits for integers

    # Step 1: Loop through each bit position
    for k in range(max_bits):
        count_k = 0  # Count of numbers with the k-th bit set

        # Count how many numbers have the k-th bit set
        for num in arr:
            if num & (1 << k):  # Check if k-th bit is set
                count_k += 1
        
        # Step 2: Calculate contribution of this bit to the total sum
        if count_k > 0:
            contribution_k = count_k * (1 << k) * (1 << (n - 1))
            total_xor_sum += contribution_k
    
    return total_xor_sum

# Example usage
array = [1, 2, 3]  # Example array
result = sum_of_subset_xor(array)
print("Sum of all subset XOR totals:", result)
