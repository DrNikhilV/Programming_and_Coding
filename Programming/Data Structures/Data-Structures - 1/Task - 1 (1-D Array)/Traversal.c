#include<stdio.h>
void main()
{
    int arr[10],i,num;

    printf("Enter a number : ");
    scanf("%d",&num);

    for(i=0;i<num;i++)
    {
        scanf("%d",&arr[i]);
    }

    for(i=0;i<num;i++)
    {
        printf("\na[%d] = %d",i,arr[i]);
    }
}