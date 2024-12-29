#include<stdio.h>
#include<stdlib.h>

struct Node 
{
    int data;
    struct Node *next;
    struct Node *prev;
};

int main() 
{
    struct Node *head = NULL;
    struct Node *tail = NULL;
    struct Node *temp = NULL;

    int num, ele, i;

    printf("Enter size of list: ");
    scanf("%d", &num);

    for (i = 0; i < num; i++) 
    {
        printf("Enter the element: ");
        scanf("%d", &ele);

        temp = (struct Node*)malloc(sizeof(struct Node));
        temp->data = ele;
        temp->next = NULL;
        temp->prev = tail;

        if (tail != NULL) 
        {
            tail->next = temp;
        } else 
        {
            head = temp;
        }

        tail = temp;
    }

    temp = head;
    while (temp != NULL) 
    {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");

    if (tail != NULL) 
    {
        tail = tail->prev;
        free(tail->next);
        tail->next = NULL;
    }

    temp = head;
    while (temp != NULL) 
    {
        printf("%d ", temp->data);
        temp = temp->next;
    }

    return 0;
}
