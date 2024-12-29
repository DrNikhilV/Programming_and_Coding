#include<stdio.h>
void main()
{
    int n,top = -1,ele;

    printf("Enter Stack size :");
    scanf("%d",&n);
    int Stack[n];

    int num;
    printf("Enter number of elements to be inserted : ");
    scanf("%d",&num);
    
    for(int i=0;i<num;i++)
    {
        scanf("%d",&Stack[i]);
        top++;
    }
    
    if(top == -1)
    {
        printf("Stack is Empty");
    }


    for(int i=top;i>=0;i--)
    {
        printf("\n%d",Stack[i]);
    }
}