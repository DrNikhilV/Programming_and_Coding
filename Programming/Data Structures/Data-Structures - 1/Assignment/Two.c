#include <stdio.h>

void rearrangeArray(int nums[], int n) {
    int result[2 * n];
    int i, j;

    for (i = 0, j = 0; i < n; i++, j += 2) {
        result[j] = nums[i];
        result[j + 1] = nums[i + n];
    }

    printf("{");
    for (i = 0; i < 2 * n; i++) {
        printf("%d", result[i]);
        if (i != 2 * n - 1) {
            printf(",");
        }
    }
    printf("}\n");
}

int main() {
    int n;
    printf("Enter the value of n: ");
    scanf("%d", &n);

    int nums[2 * n];
    printf("Enter the elements of the array:\n");
    for (int i = 0; i < 2 * n; i++) {
        scanf("%d", &nums[i]);
    }


    rearrangeArray(nums, n);

    return 0;
}
