#include<stdio.h>
#include<conio.h>
void main()
{
int n,i,a=0,b=1,c;
clrscr();
scanf("%d", &n);
for (i=1;i<=n;i++)
{
c=a+b;
a=b;
b=c;
printf(" \n Fibonacci series= %d",c);
}
getch();
}













































