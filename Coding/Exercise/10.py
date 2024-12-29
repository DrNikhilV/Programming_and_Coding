#Snake in Matrix

def longest_snake_path(matrix):
    if not matrix or not matrix[0]:
        return 0
    
    rows = len(matrix)
    cols = len(matrix[0])

    # Step 1: Create a DP table to memoize longest path starting from each cell
    dp = [[-1 for _ in range(cols)] for _ in range(rows)]

    # Step 2: Define the valid moves (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Step 3: Helper function for DFS
    def dfs(x, y):
        # If already computed, return the cached result
        if dp[x][y] != -1:
            return dp[x][y]
        
        # Start with a path length of 1 (the current cell itself)
        max_path_length = 1
        
        # Explore all four directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # Check if the new cell is within bounds and satisfies the condition
            if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] == matrix[x][y] + 1:
                # Recursively find the longest path from the new cell
                max_path_length = max(max_path_length, 1 + dfs(nx, ny))
        
        # Memoize the result
        dp[x][y] = max_path_length
        return dp[x][y]

    # Step 4: Perform DFS from every cell and find the maximum path length
    max_length = 0
    for i in range(rows):
        for j in range(cols):
            max_length = max(max_length, dfs(i, j))
    
    return max_length

# Example usage
matrix = [
    [9, 6, 5],
    [8, 7, 6],
    [7, 8, 9]
]
result = longest_snake_path(matrix)
print("The longest snake path is of length:", result)
