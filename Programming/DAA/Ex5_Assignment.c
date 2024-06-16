#include <stdio.h>
#include <limits.h>

#define N 4

void printAssignment(int assignment[N]) {
    printf("Assignment: ");
    for (int i = 0; i < N; i++) {
        printf("(%d, %d) ", i + 1, assignment[i] + 1);
    }
    printf("\n");
}

int calculateCost(int costMatrix[N][N], int assignment[N]) {
    int totalCost = 0;
    for (int i = 0; i < N; i++) {
        totalCost += costMatrix[i][assignment[i]];
    }
    return totalCost;
}

void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void generatePermutations(int costMatrix[N][N], int assignment[N], int currentWorker, int* minCost) {
    if (currentWorker == N - 1) {
        int currentCost = calculateCost(costMatrix, assignment);

        if (currentCost < *minCost) {
            *minCost = currentCost;
            printAssignment(assignment);
        }
        return;
    }

    for (int i = currentWorker; i < N; i++) {
        swap(&assignment[currentWorker], &assignment[i]);
        generatePermutations(costMatrix, assignment, currentWorker + 1, minCost);
        swap(&assignment[currentWorker], &assignment[i]);
    }
}

void exhaustiveSearch(int costMatrix[N][N]) {
    int assignment[N];
    int minCost = INT_MAX;

    for (int i = 0; i < N; i++) {
        assignment[i] = i;
    }

    generatePermutations(costMatrix, assignment, 0, &minCost);

    printf("Minimum Cost: %d\n", minCost);
}

int main() {
    int costMatrix[N][N] = {
        {9, 2, 7, 8},
        {6, 4, 3, 7},
        {5, 8, 1, 8},
        {7, 6, 9, 4}
    };

    printf("Cost Matrix:\n");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            printf("%d ", costMatrix[i][j]);
        }
        printf("\n");
    }

    printf("\n");

    printf("Exhaustive Search Approach:\n");
    exhaustiveSearch(costMatrix);

    return 0;
}
