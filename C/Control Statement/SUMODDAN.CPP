#include<stdio.h>
#include<conio.h>
void main()
{
int i,n,x=0,y=0;
clrscr();
scanf("%d", &n);
for (i=0;i<=n;i++)
{
if ((i%2)==0)
{
x=x+i;
}
else
{
y=y+i;
}
}
printf("\n sum of even= %d",x);
printf("\n sum of odd=  %d",y);
getch();
}
