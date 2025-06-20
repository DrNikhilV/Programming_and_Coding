def num_trees(n):
    dp = [1] * (n+1)
    for i in range(2, n+1):
        dp[i] = 0
        for j in range(i):
            dp[i] += dp[j] * dp[i-j-1]
    return dp[n]

print(num_trees(3))