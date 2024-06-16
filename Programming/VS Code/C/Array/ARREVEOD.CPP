#include<stdio.h>
#include<conio.h>
void main()
{
int a[100],i,n,x=0,y=0;
clrscr();
scanf("%d",&n);
for(i=0;i<n;i++)
{
scanf("%d",&a[i]);
}
for(i=0;i<n;i++)
{
if ((a[i]%2)==0)
{
x=x+1;
}
else
{
y=y+1;
}
}
printf("\n Even %d",x);
printf("\n Odd %d", y);
getch();
}
