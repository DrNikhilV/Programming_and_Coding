#include <stdio.h>

void main()
{
    int num, m, arr2[10], j, ele2, n, arr1[10], i, ele1, arr3[10], k, ele3, o, pos;

    printf("1.First Place");
    printf("\n2.Last Place");
    printf("\n3.Any position");
    printf("\n4.Delete element");
    scanf("\n%d", &num);

    switch (num)
    {
        case 1:
            printf("1.First Place");
            printf("\nEnter size of array : ");
            scanf("%d", &n);
            for (i = 0; i < n; i++)
            {
                scanf("%d", &arr1[i]);
            }
            printf("\nEnter element : ");
            scanf("%d", &ele1);
            for (i = n; i >= 0; i--)
            {
                arr1[i] = arr1[i - 1];
            }
            arr1[0] = ele1;
            n++;
            for (i = 0; i < n; i++)
            {
                printf("%d ", arr1[i]);
            }
            break;

        case 2:
            printf("\n2.Last Place");
            printf("\nEnter size of array : ");
            scanf("%d", &m);
            for (j = 0; j < m; j++)
            {
                scanf("%d", &arr2[j]);
            }
            printf("\nEnter element : ");
            scanf("%d", &ele2);
            arr2[m] = ele2;
            for (j = 0; j < m + 1; j++)
            {
                printf("%d ", arr2[j]);
            }
            break;

        case 3:
            printf("\n3.Any position");
            printf("\nEnter size of array : ");
            scanf("%d", &o);
            for (k = 0; k < o; k++)
            {
                scanf("%d", &arr3[k]);
            }
            printf("\nEnter element : ");
            scanf("%d", &ele3);
            printf("\nEnter position : ");
            scanf("%d", &pos);
            for (k = o - 1; k >= pos; k--)
            {
                arr3[k + 1] = arr3[k];
            }
            arr3[pos] = ele3;
            for (k = 0; k < o; k++)
            {
                printf("%d ", arr3[k]);
            }
            break;

        case 4:
            printf("\n4.Delete element");
            printf("\nEnter size of array : ");
            scanf("%d", &n);
            for (i = 0; i < n; i++)
            {
                scanf("%d", &arr1[i]);
            }
            printf("\nEnter element to delete: ");
            scanf("%d", &ele1);
            int found = 0;
            for (i = 0; i < n; i++)
            {
                if (arr1[i] == ele1)
                {
                    for (j = i; j < n - 1; j++)
                    {
                        arr1[j] = arr1[j + 1];
                    }
                    found = 1;
                    break;
                }
            }
            if (found)
            {
                n--;
                printf("Element deleted successfully.\n");
                for (i = 0; i < n; i++)
                {
                    printf("%d ", arr1[i]);
                }
            }
            else
            {
                printf("Element not found in the array.\n");
            }
            break;

        default:
            printf("Invalid Input");
            break;
    }
}
