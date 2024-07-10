#include <stdio.h>
#include <stdlib.h>

struct Node 
{
    int data;
    struct Node* next;
};

struct Node* top = NULL;

void push(int value) 
{
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));

    if (newNode == NULL) 
    {
        printf("Stack is Full\n");
        return;
    }

    newNode->data = value;
    newNode->next = top;
    top = newNode;
}

void pop() 
{
    if (top == NULL) 
    {
        printf("Stack is Empty\n");
        return;
    }
    struct Node* temp = top;
    top = top->next;
    printf("%d is Deleted \n", temp->data);
    free(temp);
}

void display() 
{
    if (top == NULL) 
    {
        printf("Stack is empty\n");
        return;
    }
    struct Node* temp = top;
    printf("The Stack is : \n");
    while (temp != NULL) 
    {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

int main() 
{
    int choice, value;
    while (1) 
    {
        printf("Enter your choice:\n");
        printf("1. Push\n2. Pop\n3. Display\n4. Exit\n");
        scanf("%d", &choice);
        switch (choice) 
        {
            case 1:
                printf("Enter the value to be pushed:\n");
                scanf("%d", &value);
                push(value);
                break;
            case 2:
                pop();
                break;
            case 3:
                display();
                break;
            case 4:
                exit(0);
            default:
                printf("Invalid input\n");
        }
    }
    return 0;
}
