
#include<stdio.h>
void main()
{
    int num,m,arr2[10],j,ele2,n,arr1[10],i,ele1,arr3[10],k,ele3,o,pos;

    printf("1.First Place");
    printf("\n2.Last Place");
    printf("\n3.Any position");
    scanf("\n%d",&num);

    switch (num)
    {
    case 1 : printf("1.First Place");
          printf("\nEnter size of array : ");
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            scanf("%d",&arr1[i]);
        }
        printf("\nEnter element : ");
        scanf("%d",&ele1);
        for(i=n;i>=0;i--)
        {
            arr1[i] = arr1[i-1];
        }
        arr1[0] = ele1;
        n++;
        for(i=0;i<n;i++)
        {
            printf("%d ",arr1[i]);
        }
        break;

    case 2 : printf("\n2.Last Place");
        printf("\nEnter size of array : ");
        scanf("%d",&m);
        for(j=0;j<m;j++)
        {
            scanf("%d",&arr2[j]);
        }
        printf("\nEnter element : ");
        scanf("%d",&ele2);
        arr2[m] = ele2;
        for(j=0;j<m+1;j++)
        {
            printf("%d ",arr2[j]);
        }
        break;

    case 3 : printf("\n3.Any position");
        printf("\nEnter size of array : ");
        scanf("%d",&o);  
        for(k=0;k<o;k++)
        {
            scanf("%d",&arr3[k]);
        } 
        printf("\nEnter element : ");
        scanf("%d",&ele3);
        printf("\nEnter position : ");
        scanf("%d",&pos);
        for(k=o-1;k>=pos;k--)
        {
            arr3[k+1] = arr3[k];
        }
        arr3[pos] = ele3;
        for(k=0;k<o;k++)
        {
            printf("%d ",arr3[k]);
        }
        break;
    default: printf("Invalid Input");
        break;
    }
}