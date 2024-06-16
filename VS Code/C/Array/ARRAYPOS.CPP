#include<stdio.h>
#include<conio.h>
void main()
{
int a[100],i,n;
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
printf(" \n Negative=  %d" ,a[i]);
}
else
{
printf("\n Positive= %d",a[i]);
}
}
getch();
}
