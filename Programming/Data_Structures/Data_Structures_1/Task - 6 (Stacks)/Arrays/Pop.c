#include<stdio.h>
void main()
{
    int n,top = -1,ele;

    printf("Enter Stack size :");
    scanf("%d",&n);
    int Stack[n],a[n];

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

    else
    {
        printf("\nDeleted - %d",Stack[top]);
        a[n] = Stack[top];
        top--;
    printf("\nThe stack is : ");

    for(int i=top;i>=0;i--)
    {
        printf("\n%d",Stack[i]);
    }
    }

    
        printf("\n New Stack = %d ",a[n]);
}