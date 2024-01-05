#include<stdio.h>
#include<stdlib.h>

 struct Node
 {
    int data;
    struct Node *link;
 };

    int main()
 {
    struct Node* head;
    struct Node* temp;

    head = (struct Node* )malloc(sizeof(struct Node));
    temp = (struct Node* )malloc(sizeof(struct Node));

    temp = head; 

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
            temp -> link = (struct Node* )malloc(sizeof(struct Node));
            temp = temp -> link;
        }
        }
        
        temp -> link = NULL;
        
        while(head != NULL)
        {
            printf("%d ",head->data);
            head = head -> link;
        }
    return 0;
 }
 