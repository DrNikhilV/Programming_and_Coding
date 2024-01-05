#include<stdio.h>
#include<conio.h>
void main()
{
int n,y,i,x=0;
clrscr();
scanf("%d", &n);
for (i=2;i<=n;i++)
if ((n%i)==0)
{
x=x+1;
}
if (x>1)
{
printf("\n not a prime number");
}
else
{
printf("\n it is a prime number ");
}
getch();
}













































