#include<stdio.h>
void main()
{
    int size,ele,arr[10],i,rep,num;

    printf("Enter size of the array : ");
    scanf("%d",&size);

    for(i=0;i<size;i++)
    {
        scanf("%d",&arr[i]);
    }

    printf("\nEnter the element to be added ");
    scanf("%d",&ele);

    printf("\nEnter the element to be replaced ");
    scanf("%d",&rep);

    for(i=0;i<size;i++)
    {
        if(arr[i] == rep)
        {
            num = i;
        }
    }

    arr[num] = ele;

        for(i=0;i<size;i++)
    {
        printf("%d ",arr[i]);
    }

}