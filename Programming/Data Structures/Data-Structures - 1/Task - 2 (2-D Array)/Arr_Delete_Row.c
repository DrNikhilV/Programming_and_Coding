#include<stdio.h> 
void main() 
{ 
 
    int a[10][10],i,j,row,col; 
    int ele,posi,posj; 
    //Initialize 
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
    printf("\nEnter row to be deleted : "); 
    scanf("%d",&posi); 
    for(i=0;i<row && i!=posi;i++)
     {
         for(j=0;j<col;j++)
         {
          printf("\na[%d][%d] = %d",i,j,a[i][j]); 
         }
     }
}