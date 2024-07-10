#include<stdio.h>
void main()
{
    int a[10][10][10],b[10][10][10],c[10][10][10];
    int i,j,k,row,col,wid;
    
    printf("Enter row value = ");
    scanf("%d",&row);
    
    printf("Enter column value = ");
    scanf("%d",&col);
    
    printf("Enter width value = ");
    scanf("%d",&wid);
    
    for(i=0;i<row;i++)
    {
        for(j=0;j<col;j++)
        {
            for(k=0;k<wid;k++)
            {
                scanf("%d\n",&a[i][j][k]);
            }
        }
    }
 
    for(i=0;i<row;i++)
    {
        for(j=0;j<col;j++)
        {
            for(k=0;k<wid;k++)
            {
                //printf("\na[%d][%d][%d] = %d",i,j,k,a[i][j][k]);
                printf("%d ",a[i][j][k]);
            }
        }
    }
    
    for(i=0;i<row;i++)
    {
        for(j=0;j<col;j++)
        {
            for(k=0;k<wid;k++)
            {
                scanf("%d",&b[i][j][k]);
            }
        }
    }
    for(i=0;i<row;i++)
    {
        for(j=0;j<col;j++)
        {
            for(k=0;k<wid;k++)
            {
                //printf("\nb[%d][%d][%d] = %d",i,j,k,b[i][j][k]);
                 printf("%d ",b[i][j][k]);
            }
        }
    }
    
    for(i=0;i<row;i++)
    {
        for(j=0;j<col;j++)
        {
            for(k=0;k<wid;k++)
            {
                {
                    c[i][j][k] = a[i][j][k] + b[i][j][k];
                }
            }
        }
    }
    
    for(i=0;i<row;i++)
    {
        for(j=0;j<col;j++)
        {
            for(k=0;k<wid;k++)
            {
                //printf("\nc[%d][%d][%d] = %d",i,j,k,c[i][j][k]);
                 printf("%d ",c[i][j][k]);
            }
        }
    }
}