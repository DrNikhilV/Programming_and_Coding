#include<stdio.h>
void main()
{
    int a[10][10],i,j,row,col;
    int b[2][2] = {1,2,3,4};

    //Declare
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
            printf("\na[%d][%d] = %d",i,j,a[i][j]);
        }
    }
    
    
}