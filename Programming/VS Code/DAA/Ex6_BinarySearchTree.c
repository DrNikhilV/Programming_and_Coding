#include <stdio.h>
#include <limits.h>

int min(int a, int b) {
    return (a < b) ? a : b;
}

int optimalBST(int keys[], int freq[], int n) {
    int cost[n][n];
    
    for (int i = 0; i < n; i++)
        cost[i][i] = freq[i];

    for (int L = 2; L <= n; L++) {
        for (int i = 0; i <= n - L + 1; i++) {
            int j = i + L - 1;
            cost[i][j] = INT_MAX;

            for (int r = i; r <= j; r++) {
                int c = ((r > i) ? cost[i][r - 1] : 0) +
                        ((r < j) ? cost[r + 1][j] : 0) +
                        freq[r];
                cost[i][j] = min(cost[i][j], c);
            }
        }
    }
    return cost[0][n - 1];
}

int main() {
    int keys[] = {10, 12, 20};
    int freq[] = {34, 8, 50};
    int n = sizeof(keys) / sizeof(keys[0]);
    printf("Cost of Optimal BST is: %d\n", optimalBST(keys, freq, n));
    return 0;
}