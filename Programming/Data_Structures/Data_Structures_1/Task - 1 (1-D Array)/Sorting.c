#include <stdio.h>
void main()
{
int i, j, a, n, arr[10];
printf("Enter the size of array : ");
scanf("%d", &n);
for (i = 0; i < n; ++i)
scanf("%d", &arr[i]);
for (i = 0; i < n; ++i)
{
for (j = i + 1; j < n; ++j)
{
if (arr[i] > arr[j])
{
a = arr[i];
arr[i] = arr[j];
arr[j] = a;
}
}
}
for (i = 0; i < n; ++i)
printf("%d\n",arr[i]);
}
