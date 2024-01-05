#include<stdio.h>
#include<conio.h>
void main()
{
int a[100],i,n,j,x,t;
clrscr();
scanf("%d",&n);
for(i=0;i<n;i++)
{
scanf("%d",&a[i]);
}
scanf("%d",&x);
for(i=0;i<x;i++)
{
t=a[0];
{
for(j=0;j<n;j++)
{
a[j]=a[j+1];
}
a[j-1]=t;
}
}
for(i=0;i<n;i++)
{
printf("\n %d",a[i]);
}
getch();
}