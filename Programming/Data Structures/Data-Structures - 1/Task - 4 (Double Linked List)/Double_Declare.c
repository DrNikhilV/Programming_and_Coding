#include<stdio.h>
#include<stdlib.h>

struct node
{
    int data;
    struct node *list;
    struct node *prev;
};

void print_list(struct node *head)
{   
    while(head != NULL)
    {
    printf("%d ",head -> data);
    head = head -> list;
    }
}

void main()
{
    struct node *head;
    struct node *one = NULL;
    struct node *two = NULL;
    struct node *three = NULL;
    struct node *four  = NULL;
    struct node *five  = NULL;   
    
    one = malloc(sizeof(struct node));
    two = malloc(sizeof(struct node));
    three = malloc(sizeof(struct node));
    four = malloc(sizeof(struct node));   
    five = malloc(sizeof(struct node));  


    one -> data = 2;
    two -> data = 4;
    three -> data = 6;
    four -> data = 8;
    five -> data = 10;
    
    one -> list = two;
    one -> prev = NULL;

    two -> list = three;
    two -> prev = one;

    three -> list = four;
    three -> prev = two;

    four -> list = five;
    four -> prev = three;

    five -> list = NULL;
    five -> prev = four;
    
    head = one;
    print_list(head);
}