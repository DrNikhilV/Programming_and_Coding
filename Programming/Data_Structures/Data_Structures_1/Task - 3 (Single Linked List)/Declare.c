#include<stdlib.h>
#include<stdio.h>

struct node
{
    int data;
    struct node* next;
};
typedef struct node node;

void printlist(node *head)
{
    node *temp = head;

    while(temp != NULL)
    {
        printf("%d ",temp->data);
        temp = temp->next;
    }
} 

void main()
{
    node one,two,three;
    node *head;

    one.data = 10;
    two.data = 20;
    three.data = 30;

    head = &one;
    one.next = &two;
    two.next = &three;
    three.next = NULL;

    printlist(head);
}