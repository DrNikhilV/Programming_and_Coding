#include <stdio.h>

int main() {
    int a[10], num, i;

    printf("Enter the array: ");
    for (i = 1; i <= 10; i++) {
        printf("\na[%d] = ", i);
        scanf("%d", &a[i]);
    }

    printf("Enter number to be searched: ");
    scanf("%d", &num);

    for (i = 1; i <= 10; i++) {
        if (a[i] == num) {
            printf("%d found at %d", num, i);
        }
    }

    if (i == 10) {
        printf("%d not found", num);
    }

    return 0;
}
