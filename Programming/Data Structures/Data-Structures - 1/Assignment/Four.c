#include <stdio.h>

int count(int num[], int size) {
    int count = 0;

    for (int i = 0; i < size; i++) {
        if (num[i] == 0) {
            count++;

            int j = i + 1;
            while (j < size && num[j] == 0) {
                count++;
                j++;
            }
        }
    }

    return count;
}

int main() {
    int size;
    printf("Enter the size of the array: ");
    scanf("%d", &size);

    int num[size];
    printf("Enter the elements of the array:\n");
    for (int i = 0; i < size; i++) {
        scanf("%d", &num[i]);
    }

    int zero = count(num, size);
    printf("Number of subarrays filled with 0: %d\n", zero);

    return 0;
}
