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
    struct Node* head;
    struct Node* temp;
    struct Node* temp2;

    head = (struct Node* )malloc(sizeof(struct Node));
    temp = (struct Node* )malloc(sizeof(struct Node));
    temp2 = (struct Node* )malloc(sizeof(struct Node));

    head = temp; 

    int num,ele,i;

    printf("Enter size of list : ");
    scanf("%d",&num);
    
    for(i=0;i<num;i++)
    {
        printf("Enter the element : ");
        scanf("%d",&ele);

        temp -> data = ele;
        
        if(i<num-1)
        {
            temp -> next = (struct Node* )malloc(sizeof(struct Node));
            temp -> next -> prev = temp;
            temp = temp -> next;
        }
    }

    temp -> next = NULL;
        
    int pos;
    printf("Enter the position to delete: ");
    scanf("%d",&pos);

    temp = head;
    for(i=0;i<pos-1;i++)
    {
        if(temp == NULL)
        {
            printf("Invalid position\n");
            return 0;
        }
        temp = temp -> next;
    }

    if(temp == NULL)
    {
        printf("Invalid position\n");
        return 0;
    }

    if(temp -> prev != NULL)
        temp -> prev -> next = temp -> next;
    else
        head = temp -> next;

    if(temp -> next != NULL)
        temp -> next -> prev = temp -> prev;

    free(temp);

    temp2 = head;
    while(temp2 != NULL)
    {
        printf("%d ",temp2->data);
        temp2 = temp2 -> next;
    }
        
    return 0;
}
