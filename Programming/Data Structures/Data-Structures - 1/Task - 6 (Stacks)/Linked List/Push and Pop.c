#include <stdio.h>
#include <stdlib.h>

struct Node 
{
    int data;
    struct Node* next;
};

struct Node* top = NULL;

int main() 
{
    int choice, value;
    while (1) 
    {
        printf("1. Push\n2. Pop\n3. Print and Exit\n");
        scanf("%d", &choice);

        switch (choice) 
        {
            case 1:
                printf("Enter an element: \n");
                scanf("%d", &value);
                struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));

                if (newNode == NULL) 
                {
                    printf("Stack is Full\n");
                    return 1;
                }
                newNode->data = value;
                newNode->next = top;
                top = newNode;
                break;

            case 2:
                if (top == NULL) 
                {
                    printf("Stack Underflow\n");
                } else {
                    struct Node* temp = top;
                    printf("%d popped from stack\n", temp->data);
                    top = top->next;
                    free(temp);
                }
                break;
                
            case 3:
                printf("The Stack is: \n");
                while (top != NULL) {
                    printf("%d ", top->data);
                    top = top->next;
                }
                printf("\n");
                return 0;
                
            default:
                printf("Invalid input\n");
                break;
        }
    }
}
