def maximal_square(matrix):
    if not matrix: return 0
    m, n = len(matrix), len(matrix[0])
    dp = [[0]*n for _ in range(m)]
    max_len = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1':
                if i and j:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                else:
                    dp[i][j] = 1
                max_len = max(max_len, dp[i][j])
    return max_len * max_len

print(maximal_square([["1","0","1","0","0"],
                      ["1","0","1","1","1"],
                      ["1","1","1","1","1"],
                      ["1","0","0","1","0"]]))