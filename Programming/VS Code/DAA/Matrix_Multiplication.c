#include <stdio.h>

#define N 3

void multiplyMatrix(int mat1[N][N], int mat2[N][N], int result[N][N]) {
    int i, j, k;
    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            result[i][j] = 0;
            for (k = 0; k < N; k++) {
                result[i][j] += mat1[i][k] * mat2[k][j];
            }
        }
    }
}

void displayMatrix(int mat[N][N]) {
    int i, j;
    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            printf("%d\t", mat[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int mat1[N][N] = { {1, 2, 3}, {4, 5, 6}, {7, 8, 9} };
    int mat2[N][N] = { {9, 8, 7}, {6, 5, 4}, {3, 2, 1} };
    int result[N][N];

    printf("Matrix 1:\n");
    displayMatrix(mat1);

    printf("\nMatrix 2:\n");
    displayMatrix(mat2);

    multiplyMatrix(mat1, mat2, result);

    printf("\nResultant Matrix:\n");
    displayMatrix(result);

    return 0;
}
