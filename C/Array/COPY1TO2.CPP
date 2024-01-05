#include<stdio.h>
#include<conio.h>
void main()
{
int a[100],b[100],i,n;
clrscr();
scanf("%d", &n);
for(i=0;i<n;i++)
{
scanf("%d", &a[i]);
}
for(i=0;i<n;i++)
{
b[i]=a[i];
printf("\n Array A= %d",a[i]);
printf(" Array B= %d",b[i]);
}
getch();
}
