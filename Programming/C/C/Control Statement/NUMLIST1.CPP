#include<stdio.h>
#include<conio.h>
void main()
{
int n,i,j;
clrscr();
scanf("%d", &n);
for(i=1;i<=n;i++)
{
for(j=1;j<=i;j++)
{
printf("%d",j);
}
printf("\n");
}
getch();
}
