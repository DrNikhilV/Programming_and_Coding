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

    int num, ele, i;

    printf("Enter size of list: ");
    scanf("%d", &num);

    for(i = 0; i < num; i++) 
    {
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

    if(head == NULL) 
    {
        printf("List is empty");
    } else {
        int pos;
        printf("Enter the position of the node to delete: ");
        scanf("%d", &pos);

        temp = head;
        struct Node* prev = NULL;
        for(i = 1; i < pos && temp != NULL; i++) 
        {
            prev = temp;
            temp = temp->link;
        }

        if(temp == NULL) 
        {
            printf("Invalid Position\n");
        } else {
            if(prev == NULL) 
            {
                head = temp->link;
            } else {
                prev->link = temp->link;
            }
            free(temp);
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
