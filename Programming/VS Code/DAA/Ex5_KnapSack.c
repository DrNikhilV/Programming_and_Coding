#include <stdio.h>

int max(int a, int b) {
    return (a > b) ? a : b;
}

int knapsack(int capacity, int weights[], int values[], int n) {
    if (capacity == 0 || n == 0)
        return 0;

    if (weights[n - 1] > capacity)
        return knapsack(capacity, weights, values, n - 1);

    else
        return max(values[n - 1] + knapsack(capacity - weights[n - 1], weights, values, n - 1),
                   knapsack(capacity, weights, values, n - 1));
}

int main() {
    int values[] = {60, 100, 120};
    int weights[] = {10, 20, 30};
    int capacity = 50;
    int n = sizeof(values) / sizeof(values[0]);

    int result = knapsack(capacity, weights, values, n);
    printf("Maximum value in Knapsack: %d\n", result);

    return 0;
}
