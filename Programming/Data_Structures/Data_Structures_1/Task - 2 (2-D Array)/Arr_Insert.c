#include<stdio.h>
void main()
{
    int a[10][10],i,j,row,col;
     int ele,posi,posj;
        //Initialize
    printf("Enter row value = \n");
    scanf("%d",&row);
    printf("Enter column value = ");
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
    
    printf("\nEnter the element and the positions : ");
    scanf("%d %d %d",&ele,&posi,&posj);
    
    for(i=row-1;i>=posi;i--)
    {
        for(j=col-1;j>=posj;j--)
        {
            a[i+1][j+1] = a[i][j];
            a[posi][posj] = ele;
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