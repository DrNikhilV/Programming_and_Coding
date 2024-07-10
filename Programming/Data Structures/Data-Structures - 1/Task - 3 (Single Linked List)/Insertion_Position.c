#include<stdio.h>
#include<stdlib.h>

struct Node 
{
    int data;
    struct Node* link;
};

int main() 
{
    struct Node* head = NULL;
    struct Node* temp = NULL;

    int num, ele, pos, i;

    printf("Enter size of list: ");
    scanf("%d", &num);

    for(i = 0; i < num; i++) {
        printf("Enter the element: ");
        scanf("%d", &ele);

        struct Node* newNode = (struct Node*) malloc(sizeof(struct Node));
        newNode->data = ele;
        newNode->link = NULL;

        if(head == NULL) 
        {
            head = temp = newNode;
        } else
        {
            temp->link = newNode;
            temp = temp->link;
        }
    }

    printf("Enter the position: ");
    scanf("%d", &pos);

    if(pos < 1 || pos > num + 1) 
    {
        printf("Invalid position!");
    } else 
    {
        printf("Enter the element: ");
        scanf("%d", &ele);

        struct Node* newNode = (struct Node*) malloc(sizeof(struct Node));
        newNode->data = ele;
        newNode->link = NULL;

        if(pos == 1) 
        {
            newNode->link = head;
            head = newNode;
        } else 
        {
            temp = head;
            for(i = 1; i < pos - 1; i++) 
            {
                temp = temp->link;
            }
            newNode->link = temp->link;
            temp->link = newNode;
        }

        temp = head;
        while(temp != NULL) 
        {
            printf("%d ", temp->data);
            temp = temp->link;
        }
    }

    return 0;
}
