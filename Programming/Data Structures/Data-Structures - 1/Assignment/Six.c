#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

struct Stack {
    int top;
    unsigned cap;
    char* array;
};

struct Stack* create(unsigned cap) {
    struct Stack* stack = (struct Stack*)malloc(sizeof(struct Stack));
    stack->cap = cap;
    stack->top = -1;
    stack->array = (char*)malloc(stack->cap * sizeof(char));
    return stack;
}

bool isEmpty(struct Stack* stack) {
    return stack->top == -1;
}

void push(struct Stack* stack, char item) {
    stack->array[++stack->top] = item;
}

char pop(struct Stack* stack) {
    if (isEmpty(stack)) {
        printf("Stack is empty\n");
        return '\0';
    }
    return stack->array[stack->top--];
}

bool Match(char character1, char character2) {
    if (character1 == '(' && character2 == ')')
        return true;
    if (character1 == '{' && character2 == '}')
        return true;
    if (character1 == '[' && character2 == ']')
        return true;
    return false;
}

bool valid(char* s) {
    struct Stack* stack = create(strlen(s));

    for (int i = 0; i < strlen(s); i++) {
        if (s[i] == '(' || s[i] == '{' || s[i] == '[')
            push(stack, s[i]);
        else if (s[i] == ')' || s[i] == '}' || s[i] == ']') {
            if (isEmpty(stack))
                return false;
            if (!Match(pop(stack), s[i]))
                return false;
        }
    }

    return isEmpty(stack);
}

int main() {
    char s[100];
    printf("Enter a string: ");
    scanf("%s", s);

    bool isValid = valid(s);

    if (isValid)
        printf("True\n");
    else
        printf("False\n");

    return 0;
}
