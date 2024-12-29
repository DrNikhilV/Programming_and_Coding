#include <stdio.h>
#include <string.h>

int oper(char operation[][4], int numop) {
    int x = 0;
    for (int i = 0; i < numop; i++) {
        if (strcmp(operation[i], "++X") == 0) {
            x++;
        } else if (strcmp(operation[i], "--X") == 0) {
            x--;
        } else if (strcmp(operation[i], "X++") == 0) {
            x++;
        } else if (strcmp(operation[i], "X--") == 0) {
            x--;
        }
    }
    return x;
}

int main() {
    char operation[][4] = {"++X", "++X", "--X"};
    int numop = sizeof(operation) / sizeof(operation[0]);
    int result = oper(operation, numop);
    printf("%d\n", result);
    
    return 0;
}
