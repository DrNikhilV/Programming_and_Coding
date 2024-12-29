#include<stdio.h>
void main()
{
    int a[10][10],i,j,row,col;
     int ele,posi,posj;
    
    printf("Enter row value = ");
    scanf("%d",&row);
    printf("\nEnter column value = ");
    scanf("%d",&col);
    
    for(i=0;i<row;i++)
    {
        for(j=0;j<col;j++)
        {
            scanf("%d",&a[i][j]);
        }
    }
    for(i=0;i<row;i++)
    {
        for(j=0;j<col;j++)
        {
           printf("%d ",a[i][j]);
        }
    }
        printf("\nEnter value and position : ");
        scanf("%d %d %d",&ele,&posi,&posj);
    for(i=0;i<row;i++)
    {
        for(j=0;j<col;j++)
        {
            if(i == posi && j == posj)
            {
                a[i][j] = ele;
            }
        }
    }
    for(i=0;i<row;i++)
    {
        for(j=0;j<col;j++)
        {
            printf("%d ",a[i][j]);
        }
    }
}