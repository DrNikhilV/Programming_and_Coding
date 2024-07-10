#include<stdio.h>
void main()
{
    int num,arr[10][10],n,i,j,k;
    int temp;
    printf("Enter size of array : \n");
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            scanf("%d",&arr[i][j]);
        }
    }
printf("Column-wise\n");
    for (i = 0; i < n; i++)
    {
    for (j = 0; j < n; j++)
    {
        if(arr[i][j] > arr[i+1][j])
        {
           temp = arr[i][j];
            arr[i][j] = arr[i+1][j];
            arr[i+1][j] = temp;
        }
    }
    }
    for (i = 0; i < n; ++i)
{
    for(j=0;j<n;j++)
    {
        printf("%d\n",arr[i][j]);
    }
}

}