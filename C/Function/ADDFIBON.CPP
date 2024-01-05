#include<stdio.h>
#include<conio.h>

void add()

{
int a,b,c;
printf("\n Enter a value= ");
scanf("%d",&a);
printf("\n Enter b value= ");
scanf("%d",&b);
c=a+b;
printf("the addition value is = %d",c);
}

void fib()

{
int n,i,a=0,b=1,c;
printf("\n enter n value = ");
scanf("%d", &n);
for (i=1;i<=n;i++)
{
c=a+b;
a=b;
b=c;
printf(" \n Fibonacci series= %d",c);
}
}
void dig()

{
int i,x=0;
printf("\n Enter Number= ");
scanf("%d", &i);
while (i>0)
{
i=i/10;
x=x+1;
}
printf("\n Number of Digits= %d",x);
}

void main()
{
clrscr();
add();
fib();
dig();
getch();
}