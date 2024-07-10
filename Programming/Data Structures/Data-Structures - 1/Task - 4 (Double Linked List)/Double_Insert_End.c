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
            temp = temp -> next;
        }
        }

        temp -> next = NULL;
        
    int no;
    printf("Enter the number : ");
    scanf("%d",&no);

    while (temp->next != NULL) 
       {
        temp = temp->next;
       }

    temp -> next = temp2;
    
    temp2 -> data = no;
    temp2  -> next = NULL;
    temp2 -> prev = temp;

        while(head != NULL)
        {
            printf("%d ",head->data);
            head = head -> next;
        }
        
    return 0;
 }
 