#include<stdio.h>

int main() {
    int a[10][10], i, j, row, col;
    int ele, posi, posj;

    // Initialize
    printf("Enter row value: ");
    scanf("%d", &row);
    printf("Enter column value: ");
    scanf("%d", &col);

    // Input the elements
    printf("Enter the elements:\n");
    for (i = 0; i < row; i++) {
        for (j = 0; j < col; j++) {
            scanf("%d", &a[i][j]);
        }
    }

    // Display the original array
    printf("Original array:\n");
    for (i = 0; i < row; i++) {
        for (j = 0; j < col; j++) {
            printf("%d ", a[i][j]);
        }
        printf("\n");
    }

    // Input the element and position for deletion
    printf("Enter the element and the positions for deletion: ");
    scanf("%d %d %d", &ele, &posi, &posj);

    // Modify the array by excluding the element at the specified position
    int new_row = row - 1;
    int new_col = col - 1;
    int new_array[10][10];

    for (i = 0; i < row; i++) {
        for (j = 0; j < col; j++) {
            if (i != posi || j != posj) {
                if (i > posi && j > posj) {
                    new_array[i - 1][j - 1] = a[i][j];
                }
                else if (i > posi) {
                    new_array[i - 1][j] = a[i][j];
                }
                else if (j > posj) {
                    new_array[i][j - 1] = a[i][j];
                }
                else {
                    new_array[i][j] = a[i][j];
                }
            }
        }
    }

    // Display the modified array after deletion
    printf("Array after deletion:\n");
    for (i = 0; i < new_row; i++) {
        for (j = 0; j < new_col; j++) {
            printf("%d ", new_array[i][j]);
        }
        printf("\n");
    }

    return 0;
}
