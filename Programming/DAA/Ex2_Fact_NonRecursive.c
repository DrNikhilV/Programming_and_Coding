#include <stdio.h>

int main() {
    int num, i;
    int result = 1;

    printf("Enter a number: ");
    scanf("%d", &num);

    for (i = 1; i <= num; ++i) {
        result *= i;
    }

    printf("Factorial of %d is: %d\n", num, result);

    return 0;
}
