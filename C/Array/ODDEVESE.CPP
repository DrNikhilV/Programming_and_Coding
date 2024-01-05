#include<stdio.h>
#include<conio.h>
void main()
{
int a[100],d[100],c[100],i,n,x=0,y=0;
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
d[x]=a[i];
x=x+1;
}
else
{
c[y]=a[i];
y=y+1;
}
}
for (i=0;i<x;i++)
{
printf("\n Even= %d",d[i]);
}
for (i=0;i<y;i++)
{
printf("\n Odd= %d",c[i]);
}
getch();
}
