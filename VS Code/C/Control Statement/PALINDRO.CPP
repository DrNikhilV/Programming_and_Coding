#include<stdio.h>
#include<conio.h>
void main()
{
int i,x=0,t,z;
clrscr();
scanf("%d", &i);
z=i;
while (i>0)
{
t=i%10;
x=(x*10)+t;
i=i/10;
}
printf("%d",x);
if (z==x)
{
printf(" palindrome");
}
else
{
printf("\n not");
}

getch();
}
