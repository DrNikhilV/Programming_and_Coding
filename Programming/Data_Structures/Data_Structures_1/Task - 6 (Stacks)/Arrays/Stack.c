#include <stdio.h>

int Push(int size, int* stack, int top)
{
    int n;
    if (top == size-1)
    {
        printf("Stack is Full");
    }
    else 
    {
        top++;
        printf("Enter element: ");
        scanf("%d", &n);
        stack[top] = n;
    }
    return top;
}

int Pop(int* stack, int top)
{
    if (top == -1)
    {
        printf("Stack is Empty");
    }
    else
    {
        printf("Deleted element: ", stack[top]);
        top--;
    }
    return top;
}

void Display(int* stack, int top)
{
    for (int i=top; i>=0; i--)
    {
        printf("%d -> ", stack[i]);
    }
    printf("NULL");
}

int main()
{
    int size, choice, num=1, top=-1;
    printf("Enter the size of stack: ");
    scanf("%d", &size);

    int stack[size];

    while (num)
    {
        printf("\nStack Operations\n");
        printf("1. Push\n");
        printf("2. Pop\n");
        printf("3. Display\n");
        printf("4. Exit\n");
        printf("Enter choice: ");
        scanf("%d", &choice);

        switch(choice)
        {
            case 1:
                top = Push(size, stack, top);
                break;
            case 2:
                top = Pop(stack, top);
                break;
            case 3:
                Display(stack, top);
                break;
            case 4:
                printf("Exit Succesful\n");
                break;
        }
    }

    return 0;
}
