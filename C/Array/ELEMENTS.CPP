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
printf("\n Number %d",a[i]);
}
getch();
}