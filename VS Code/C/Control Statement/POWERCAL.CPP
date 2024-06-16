#include<stdio.h>
#include<conio.h>
void main()
{
int i,n,v,j,y=0;
clrscr();
scanf("%d", &n);
for (i=1;i<=n;i++)
{
v=1;
for (j=1;j<=i;j++)
{
v=v*i;
}
y=y+v;
}
printf("\n %d",y);
getch();
}
