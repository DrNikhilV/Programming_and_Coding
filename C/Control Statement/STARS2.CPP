#include<stdio.h>
#include<conio.h>
void main()
{
int i,n,j;
clrscr();
printf(" Enter number of stars= ");
scanf("%d", &n);
for(i=0;i<n;i++)
{
for(j=0;j<n;j++)
{
if (((j<1) || (j>=n-1)) || ((i<1) || (i>=n-1)))
{
printf(" * ");
}
else if((i<2) || (i==n-3) || (i==n-2) || (i<3))
{
printf(" | ");
}
else if(i<4)
{
printf(" [ ");
}
else if(i==(n-4))
{
printf(" ] ");
}
else
{
printf("   ");
}
}
printf("\n");
}
getch();
}