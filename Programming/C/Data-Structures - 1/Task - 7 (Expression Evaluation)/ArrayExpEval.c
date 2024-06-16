#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#define MAX 100

struct Stack {
    int arr[MAX];
    int top;
};

void initStack(struct Stack* stack) {
    stack->top = -1;
}

int isFull(struct Stack* stack) {
    return stack->top == MAX - 1;
}

int isEmpty(struct Stack* stack) {
    return stack->top == -1;
}

void push(struct Stack* stack, int data) {
    if (isFull(stack)) {
        printf("Stack overflow\n");
        return;
    }
    stack->arr[++stack->top] = data;
}

int pop(struct Stack* stack) {
    if (isEmpty(stack)) {
        printf("Stack underflow\n");
        return -1;
    }
    return stack->arr[stack->top--];
}

int peek(struct Stack* stack) {
    if (isEmpty(stack)) {
        printf("Stack is empty\n");
        return -1;
    }
    return stack->arr[stack->top];
}

int evaluatePostfix(char* exp) {
    struct Stack stack;
    initStack(&stack);

    for (int i = 0; exp[i]; i++) {
        if (isdigit(exp[i])) {
            push(&stack, exp[i] - '0');
        } else {
            int val1 = pop(&stack);
            int val2 = pop(&stack);
            switch (exp[i]) {
                case '+': push(&stack, val2 + val1); break;
                case '-': push(&stack, val2 - val1); break;
                case '*': push(&stack, val2 * val1); break;
                case '/': push(&stack, val2 / val1); break;
            }
        }
    }
    return pop(&stack);
}

int main() {
    char exp[] = "231*+9-";
    printf("Postfix evaluation: %d\n", evaluatePostfix(exp));
    return 0;
}
