#Matrix Diagonal Sum

def diagonal_sum(matrix):
    n = len(matrix)
    total_sum = 0
    
    # Loop through the matrix
    for i in range(n):
        # Add primary diagonal element
        total_sum += matrix[i][i]
        
        # Add secondary diagonal element
        total_sum += matrix[i][n - 1 - i]
    
    # If the matrix has odd size, subtract the middle element (added twice)
    if n % 2 == 1:
        middle_index = n // 2
        total_sum -= matrix[middle_index][middle_index]
    
    return total_sum

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result = diagonal_sum(matrix)
print("The sum of the matrix diagonals is:", result)
