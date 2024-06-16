#include<stdio.h>
#include<conio.h>
void main()
{
int a[100],i,n,y=0;
clrscr();
scanf("%d",&n);
for(i=0;i<n;i++)
{
scanf("%d",&a[i]);
}
for(i=0;i<n;i++)
{
if (a[i]<0)
{
y=y+a[i];
}
}
printf("\n Number %d",y);
getch();
}