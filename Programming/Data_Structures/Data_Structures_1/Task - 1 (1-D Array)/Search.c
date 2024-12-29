#include<stdio.h>
void main()
{
    int ele,size,arr[10],i;

    printf("Enther the size of array : ");
    scanf("%d",&size);

    for(i=0;i<size;i++)
    {
        scanf("%d",&arr[i]);
    }
    printf("\nEnter the element to be found : ");
    scanf("%d",&ele);

    for(i=0;i<size;i++)
    {
        if(arr[i] == ele)
        {
            printf("\nThe element %d exists",ele);
        }
    }
}