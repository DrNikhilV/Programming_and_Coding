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
    } else 
    {
        temp = head;
        head = head->link;
        free(temp);

        temp = head;
        while(temp != NULL) 
        {
            printf("%d ", temp->data);
            temp = temp->link;
        }
    }

    return 0;
}
