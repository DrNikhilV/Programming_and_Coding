#include<stdio.h>
#include<conio.h>
void main()
{
int a[100],i,n,j,t;
clrscr();
scanf("%d",&n);
for(i=0;i<n;i++)
{
scanf("%d",&a[i]);
}
for(i=0;i<n;i++)
{
for(j=i+1;j<n;j++)
{
if(a[i]<a[j])
{
t=a[i];
a[i]=a[j];
a[j]=t;
}
}
}
for(i=0;i<n;i++)
{
printf("\n %d",a[i]);
}
printf("\n second max %d", a[1]);
getch();
}
