#include<stdio.h>
#include<conio.h>
void main()
{
int a[100],i,n,j,x,t;
clrscr();
printf("\n No of Elements= ");
scanf("%d",&n);
for(i=0;i<n;i++)
{
scanf("%d",&a[i]);
}
printf("\n No of times to be rotated= ");
scanf("%d",&x);
for(i=0;i<x;i++)
{
t=a[n-1];
{
for(j=n;j>0;j--)
{
a[j]=a[j-1];
}
a[j]=t;
}
}
for(i=0;i<n;i++)
{
printf("\n %d",a[i]);
}
getch();
}