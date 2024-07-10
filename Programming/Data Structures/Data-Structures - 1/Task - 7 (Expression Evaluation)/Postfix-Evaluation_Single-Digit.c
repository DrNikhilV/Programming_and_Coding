#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

typedef struct Stack
{
    int top;
    unsigned capacity;
    int* array;
} Stack;

Stack* createStack(unsigned capacity)
{
    Stack* stack = (Stack*) malloc(sizeof(Stack));
    if (!stack)
    {
        return NULL;
    }
    stack->top = -1;
    stack->capacity = capacity;
    stack->array = (int*) malloc(stack->capacity * sizeof(int));
    if (!stack->array)
    {
        return NULL;
    }
    return stack;
}

int isEmpty(Stack* stack)
{
    return stack->top == -1;
}

int peek(Stack* stack)
{
    return stack->array[stack->top];
}

int pop(Stack* stack)
{
    if (!isEmpty(stack))
    {
        return stack->array[stack->top--];
    }
    return -1;
}

void push(Stack* stack, int op)
{
    stack->array[++stack->top] = op;
}

int evaluatePostfix(char* exp)
{
    Stack* stack = createStack(strlen(exp));
    if (!stack)
    {
        return -1;
    }
    int i;
    int operand_count = 0;
    int last_operand = 0;
    for (i = 0; exp[i]; ++i)
    {
        if (isspace(exp[i]))
        {
            continue;
        }
        else if (isdigit(exp[i]))
        {
            int num = 0;
            while (isdigit(exp[i]))
            {
                num = num * 10 + (int)(exp[i] - '0');
                i++;
            }
            i--;
            push(stack, num);
            operand_count++;
            last_operand = num;
        }
        else
        {
            return -1; 
        }
    }
    if (operand_count != 1) {
        return -1;
    }
    int result = last_operand;
    free(stack->array);
    free(stack);
    return result;
}

int main()
{
    char s[100];
    printf("Enter the postfix expression: ");
    fgets(s, 100, stdin);
    s[strcspn(s, "\n")] = '\0';
    int result = evaluatePostfix(s);
    if (result == -1)
    {
        printf("Invalid expression");
    }
    else
    {
        printf("%d", result);
    }
    return 0;
}
