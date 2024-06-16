#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

struct Node {
    int data;
    struct Node* next;
};

struct Stack {
    struct Node* top;
};

void initStack(struct Stack* stack) {
    stack->top = NULL;
}

int isEmpty(struct Stack* stack) {
    return stack->top == NULL;
}

void push(struct Stack* stack, int data) {
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    if (!new_node) {
        printf("Stack overflow\n");
        return;
    }
    new_node->data = data;
    new_node->next = stack->top;
    stack->top = new_node;
}

int pop(struct Stack* stack) {
    if (isEmpty(stack)) {
        printf("Stack underflow\n");
        return -1;
    }
    struct Node* temp = stack->top;
    int popped = temp->data;
    stack->top = stack->top->next;
    free(temp);
    return popped;
}

int peek(struct Stack* stack) {
    if (isEmpty(stack)) {
        printf("Stack is empty\n");
        return -1;
    }
    return stack->top->data;
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
